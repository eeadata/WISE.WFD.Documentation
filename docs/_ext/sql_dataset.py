# -*- coding: utf-8 -*-
"""
sql_dataset.py — custom Sphinx extension.

Provides a single directive, `sql-dataset`, that renders the full
documentation of one dataset table by querying a SQLAlchemy-accessible
database at build time:

    - the table name (heading)
    - one combined table listing every field (Attribute / Type /
      Multiplicity / Definition)
    - the table's own description
    - the table-level quality controls (as a table, no extra heading)
    - one sub-heading per field, each followed directly by that
      field's quality controls (as a table, no extra heading)

Usage (MyST):

    ```{sql-dataset} GWAssociatedProtectedArea WFDProtectedArea
    :connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
    ```

The second argument is the dataflow's short code (e.g. WFDProtectedArea,
WFDMonitoring, WFDRiverBasinDistrict), used to disambiguate tables whose
name is reused across dataflows (Document, dcMetadata).

Expects two tables in the database:

    metadata(tableName, columnName, columnPosition, columnDataType,
             multiplicity, metadataInfo, objectType, dataflowId,
             dataflowCode)
    qc(Table, Field, Code, "QC Name", "QC Description", Message,
       Expression, "Type of QC", "Severity Level", "Creation Mode",
       Status, Valid, dataflowId, dataflowCode)
"""

import re

import sqlalchemy
from docutils import nodes
from docutils.parsers.rst.directives import unchanged
from sphinx import addnodes
from sphinx.util.docutils import SphinxDirective


def _slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def _dataflow_filter(table_name, dataflow_code, **extra_params):
    """Builds the (params, sql_suffix) pair used to optionally scope a
    query by dataflowCode, avoiding duplicating this logic at every
    call site. extra_params lets callers add e.g. the field name."""
    params = {"t": table_name, **extra_params}
    sql_suffix = ""
    if dataflow_code:
        sql_suffix = " AND dataflowCode=:dfcode"
        params["dfcode"] = dataflow_code
    return params, sql_suffix


def _build_table(headers, rows, widths):
    ncols = len(headers)
    table = nodes.table()
    table["classes"] += ["colwidths-given"]
    tgroup = nodes.tgroup(cols=ncols)
    table += tgroup
    for w in widths:
        tgroup += nodes.colspec(colwidth=w)

    thead = nodes.thead()
    tgroup += thead
    header_row = nodes.row()
    for h in headers:
        entry = nodes.entry()
        entry += nodes.paragraph(text=str(h))
        header_row += entry
    thead += header_row

    tbody = nodes.tbody()
    tgroup += tbody
    for row in rows:
        row_node = nodes.row()
        for cell in row:
            entry = nodes.entry()
            if isinstance(cell, list):
                # pre-built inline nodes (e.g. a glossary term reference)
                para = nodes.paragraph()
                para += cell
                entry += para
            else:
                entry += nodes.paragraph(text="" if cell is None else str(cell))
            row_node += entry
        tbody += row_node

    return table


_TYPE_LENGTH_RE = re.compile(r"^(.*)\((\d+)\)$")


class SqlDatasetDirective(SphinxDirective):
    """Renders one dataset table: an all-fields overview table, the
    table description, the table-level QCs, and one sub-section per
    field with just its QCs - all pulled live from the database."""

    required_arguments = 1  # table name, e.g. "ProtectedArea"
    optional_arguments = 1  # optional dataflow code (e.g. "WFDProtectedArea") -
                             # disambiguates when the same table name is
                             # reused across different dataflows
    final_argument_whitespace = True
    option_spec = {
        "connection_string": unchanged,
        "id_prefix": unchanged,  # override auto-generated anchor prefix
        "dataflow": unchanged,   # alternative way to pass the dataflow code
    }
    has_content = False

    def _type_cell(self, raw_type):
        """Builds the Type column cell: a real cross-reference link to
        the glossary term (built the same way Sphinx's own :term: role
        does internally, via a pending_xref node), with any trailing
        length (e.g. "(4000)") appended as plain text right after it -
        matching the "string254"-style rendering used across the
        project."""
        m = _TYPE_LENGTH_RE.match(raw_type)
        base, length = (m.group(1), m.group(2)) if m else (raw_type, None)

        xref = addnodes.pending_xref(
            "", refdomain="std", reftype="term", reftarget=base.lower(),
            refexplicit=False, refwarn=True,
        )
        xref += nodes.Text(base)
        nodelist = [xref]
        if length:
            nodelist.append(nodes.Text(length))
        return nodelist

    def run(self):
        table_name = self.arguments[0].strip()
        dataflow_code = None
        if len(self.arguments) > 1:
            dataflow_code = self.arguments[1].strip()
        dataflow_code = self.options.get("dataflow", dataflow_code)

        conn_str = self.options.get("connection_string") or getattr(
            self.env.config, "sqltable_connection_string", None
        )
        if not conn_str:
            error = self.state_machine.reporter.error(
                "sql-dataset: no :connection_string: given and no "
                "sqltable_connection_string configured.",
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno,
            )
            return [error]

        params, dataflow_filter_sql = _dataflow_filter(table_name, dataflow_code)

        engine = sqlalchemy.create_engine(conn_str)
        with engine.connect() as conn:
            desc_row = conn.execute(
                sqlalchemy.text(
                    "SELECT metadataInfo FROM metadata "
                    f"WHERE objectType='table' AND tableName=:t{dataflow_filter_sql}"
                ),
                params,
            ).fetchone()
            description = desc_row[0] if desc_row else ""

            table_qcs = conn.execute(
                sqlalchemy.text(
                    'SELECT Code, "Severity Level", Message FROM qc '
                    f'WHERE "Table"=:t AND "Field"=\'\'{dataflow_filter_sql} ORDER BY Code'
                ),
                params,
            ).fetchall()

            fields = conn.execute(
                sqlalchemy.text(
                    "SELECT columnName, columnDataType, multiplicity, metadataInfo "
                    f"FROM metadata WHERE objectType='column' AND tableName=:t{dataflow_filter_sql} "
                    "ORDER BY columnPosition"
                ),
                params,
            ).fetchall()

        id_prefix = self.options.get("id_prefix") or f"sql-{_slug(table_name)}"

        top_section = nodes.section(ids=[id_prefix])
        top_section += nodes.title(text=table_name)

        # --- combined all-fields table (Attribute | Type | M | Definition) ---
        if fields:
            top_section += _build_table(
                ["Attribute", "Type", "M", "Definition"],
                [
                    (column_name, self._type_cell(dtype), mult, field_desc)
                    for column_name, dtype, mult, field_desc in fields
                ],
                widths=[18, 15, 7, 60],
            )

        # --- table description ---
        if description:
            top_section += nodes.paragraph(text=description)

        # --- table-level QCs (no heading) ---
        if table_qcs:
            top_section += _build_table(
                ["Code", "Severity", "Description"],
                list(table_qcs),
                widths=[10, 15, 75],
            )

        # --- one sub-section per field: title + QCs only (no heading, no def table) ---
        for column_name, dtype, mult, field_desc in fields:
            field_id = f"{id_prefix}-{_slug(column_name)}"
            field_section = nodes.section(ids=[field_id])
            field_section += nodes.title(text=column_name)

            field_qc_params, _ = _dataflow_filter(table_name, dataflow_code, f=column_name)
            with engine.connect() as conn:
                field_qcs = conn.execute(
                    sqlalchemy.text(
                        'SELECT Code, "Severity Level", Message FROM qc '
                        f'WHERE "Table"=:t AND "Field"=:f{dataflow_filter_sql} ORDER BY Code'
                    ),
                    field_qc_params,
                ).fetchall()

            if field_qcs:
                field_section += _build_table(
                    ["Code", "Severity", "Description"],
                    list(field_qcs),
                    widths=[10, 15, 75],
                )

            top_section += field_section

        return [top_section]


def setup(app):
    app.add_directive("sql-dataset", SqlDatasetDirective)
    return {"version": "0.2", "parallel_read_safe": True, "parallel_write_safe": True}

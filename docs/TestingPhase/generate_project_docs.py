"""
generate_project_docs.py
-------------------------
Generates a Sphinx project subfolder with this structure:

    MonitoringSite
    |-- Spatial QCs
    |   |-- Table QCs
    |   `-- Field QCs
    `-- Descriptive QCs
        |-- Table QCs
        `-- Field QCs

Each top section (Spatial QCs / Descriptive QCs) is read from its own
CSV/Excel file. Within each section, QCs whose "Field" column is empty
become "Table QCs" pages (one per table); QCs whose "Field" column is
filled become "Field QCs" pages (one per table, split into a
sub-section per field).

This version does NOT use command-line arguments — everything is
configured in the CONFIGURATION block below. Just edit the values and
run:

    python generate_project_docs.py
"""

import csv
import os
import sys
from collections import OrderedDict

# --------------------------------------------------------------------------
# CONFIGURATION — edit these values
# --------------------------------------------------------------------------
PROJECT_NAME = "QualityControl"       # name of the project (= name of its folder)
DOCS_ROOT = "MonitoringSite"          # created automatically if it doesn't exist yet

# Path from the Sphinx *source root* (the "docs" folder) down to where
# this script writes its output. Used to build absolute-style include
# paths (leading "/") so nested includes (WFDMonitoring.md -> section
# index.md -> table_qcs.md/field_qcs.md) resolve correctly regardless of
# nesting depth. Adjust if you move this script to a different folder.
SOURCE_ROOT_PREFIX = "/TestingPhase/MonitoringSite/QualityControl"

# Folder containing one CSV/Excel per section (e.g. "Spatial_QCs.csv",
# "Descriptive_QCs.csv", "Documents_QCs.csv"). Every .csv/.xlsx/.xls file
# found here becomes its own section automatically — no need to list
# filenames by hand. The section name is taken from the filename itself
# (a trailing "_QCs"/"_QC" is stripped, and underscores become spaces),
# so "Spatial_QCs.csv" -> folder "spatial", caption "Spatial QCs".
QC_FILES_DIR = "MonitoringSite/QC files"


def discover_sections(qc_dir):
    """Scans qc_dir for CSV/Excel files and turns each one into a
    (input_path, section_folder, section_caption) tuple, sorted
    alphabetically by filename."""
    sections = []
    if not os.path.isdir(qc_dir):
        return sections
    for filename in sorted(os.listdir(qc_dir)):
        ext = os.path.splitext(filename)[1].lower()
        if ext not in (".csv", ".xlsx", ".xls"):
            continue
        base = os.path.splitext(filename)[0]
        name = base
        for suffix in ("_QCs", "_QC", "-QCs", "-QC"):
            if name.lower().endswith(suffix.lower()):
                name = name[: -len(suffix)]
                break
        name = name.replace("_", " ").replace("-", " ").strip()
        folder = slug(name).strip("_").lower()
        caption = f"{name} QCs"
        sections.append((os.path.join(qc_dir, filename), folder, caption))
    return sections


def slug(name: str) -> str:
    return "".join(c if c.isalnum() else "_" for c in name)


def md_escape(value) -> str:
    if value is None:
        return ""
    text = str(value)
    text = text.replace("\\", "\\\\")
    for ch in ("_", "*", "`"):
        text = text.replace(ch, "\\" + ch)
    return text


def clean(value) -> str:
    if value is None:
        return "\\-"
    text = md_escape(value).strip()
    if not text:
        return "\\-"
    return " ".join(text.split())


def render_list_table(title, header, rows, widths):
    widths_str = " ".join(str(w) for w in widths)
    lines = []
    opening = f"```{{list-table}} {title}" if title else "```{list-table}"
    lines.append(opening)
    lines.append(f":widths: {widths_str}")
    lines.append(":header-rows: 1")
    lines.append("")
    lines.append("* - " + "\n  - ".join(header))
    for row in rows:
        lines.append("* - " + "\n  - ".join(clean(v) for v in row))
    lines.append("```")
    lines.append("")
    return lines


def read_rows(path):
    ext = os.path.splitext(path)[1].lower()
    if ext in (".xlsx", ".xls"):
        try:
            import openpyxl
        except ImportError:
            sys.exit(
                "Reading Excel files requires openpyxl. Install it with:\n"
                "    pip install openpyxl --break-system-packages"
            )
        wb = openpyxl.load_workbook(path, data_only=True)
        ws = wb.active
        rows_iter = ws.iter_rows(values_only=True)
        header = [str(h).strip() if h is not None else "" for h in next(rows_iter)]
        rows = []
        for values in rows_iter:
            if all(v is None for v in values):
                continue
            rows.append(dict(zip(header, values)))
        return rows
    else:
        with open(path, encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]


def group_by_table(rows):
    tables = OrderedDict()
    for row in rows:
        table = (row.get("Table") or "").strip()
        if not table:
            continue
        tables.setdefault(table, []).append(row)
    return tables


def qc_field(row):
    return (row.get("Field") or "").strip()


def render_qc_rows(qcs):
    out = []
    for qc in qcs:
        code = qc.get("Code") or ""
        severity = qc.get("Severity Level") or ""
        description = qc.get("Message") or ""
        out.append((code, severity, description))
    return out


def render_table_qcs_doc(table_name, qcs):
    """QCs whose 'Field' column is empty -> table-level QCs content,
    meant to be embedded via {include} (no own H1/H2 — the parent
    section index.md provides the table-name heading)."""
    table_level_qcs = [qc for qc in qcs if not qc_field(qc)]

    lines = ["##### Table QCs", ""]
    lines.append("**Description:** *(no description available — generated from a QC export only)*")
    lines.append("")
    if table_level_qcs:
        lines += render_list_table(
            None,
            ["Code", "Severity", "Description"],
            render_qc_rows(table_level_qcs),
            widths=[10, 15, 75],
        )
    else:
        lines.append("*(no table QCs)*")
        lines.append("")
    return lines, len(table_level_qcs)


def render_field_qcs_doc(table_name, qcs):
    """QCs whose 'Field' column is filled -> field-level QCs page,
    grouped by field, in first-seen order."""
    fields = OrderedDict()
    for qc in qcs:
        if not qc_field(qc):
            continue
        fields.setdefault(qc_field(qc), []).append(qc)

    lines = ["##### Field QCs", ""]
    if fields:
        for field_name, field_qcs in fields.items():
            lines.append(f"###### {field_name}")
            lines.append("")
            lines += render_list_table(
                None,
                ["Code", "Severity", "Description"],
                render_qc_rows(field_qcs),
                widths=[10, 15, 75],
            )
    else:
        lines.append("*(no field QCs)*")
        lines.append("")
    return lines, sum(len(v) for v in fields.values())


def render_index(title, toctree_blocks):
    """toctree_blocks: list of (caption, glob_prefix, doc_names)."""
    lines = [f"# {title}", ""]
    for caption, glob_prefix, doc_names in toctree_blocks:
        lines += [
            "```{toctree}",
            ":maxdepth: 2",
            f":caption: {caption}",
            ":glob:",
            "",
        ]
        for name in doc_names:
            lines.append(f"{glob_prefix}/{slug(name)}")
        lines.append("```")
        lines.append("")
    return "\n".join(lines)


def generate_section(project_dir, input_path, section_folder, section_caption):
    """Generates one section (Spatial QCs / Descriptive QCs): reads its
    CSV, and for every table found writes 'table_qcs.md' + 'field_qcs.md'
    in a subfolder. The section's own index.md embeds both directly via
    {include}, one '## TableName' block per table (no separate pages,
    no toctree navigation to click through)."""
    if not os.path.exists(input_path):
        print(f"Skipping '{section_caption}': file not found ({input_path})")
        return None

    rows = read_rows(input_path)
    if not rows:
        print(f"Skipping '{section_caption}': no rows found in {input_path}.")
        return None

    tables = group_by_table(rows)
    if not tables:
        print(f"Skipping '{section_caption}': no 'Table' column values found in {input_path}.")
        return None

    section_dir = os.path.join(project_dir, section_folder)

    index_lines = []

    for table_name, qcs in tables.items():
        table_dir = os.path.join(section_dir, slug(table_name))
        os.makedirs(table_dir, exist_ok=True)

        table_lines, n_table = render_table_qcs_doc(table_name, qcs)
        table_qcs_path = os.path.join(table_dir, "table_qcs.md")
        with open(table_qcs_path, "w", encoding="utf-8") as f:
            f.write("\n".join(table_lines))
        print(f"Generated: {table_qcs_path}  ({n_table} table QCs)")

        field_lines, n_field = render_field_qcs_doc(table_name, qcs)
        field_qcs_path = os.path.join(table_dir, "field_qcs.md")
        with open(field_qcs_path, "w", encoding="utf-8") as f:
            f.write("\n".join(field_lines))
        print(f"Generated: {field_qcs_path}  ({n_field} field QCs)")

        index_lines.append(f"#### {table_name}")
        index_lines.append("")
        index_lines.append(
            "```{include} " + f"{SOURCE_ROOT_PREFIX}/{section_folder}/{slug(table_name)}/table_qcs.md"
        )
        index_lines.append("```")
        index_lines.append("")
        index_lines.append(
            "```{include} " + f"{SOURCE_ROOT_PREFIX}/{section_folder}/{slug(table_name)}/field_qcs.md"
        )
        index_lines.append("```")
        index_lines.append("")

    section_index_path = os.path.join(section_dir, "index.md")
    with open(section_index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines))
    print(f"Generated: {section_index_path}")

    return section_folder


def main():
    project_dir = os.path.join(DOCS_ROOT, PROJECT_NAME)
    section_folders = []

    sections = discover_sections(QC_FILES_DIR)
    if not sections:
        print(f"No CSV/Excel files found in '{QC_FILES_DIR}'.")
        return

    for input_path, section_folder, section_caption in sections:
        result = generate_section(project_dir, input_path, section_folder, section_caption)
        if result:
            section_folders.append((section_caption, result))

    if not section_folders:
        print("Nothing generated — check that your CSV/Excel files exist and have data.")
        return

    print(f"\nDone. {len(section_folders)} section(s) generated under {project_dir}/")


if __name__ == "__main__":
    main()

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os
from pybtex.style.sorting import BaseSortingStyle
from pybtex.style.formatting.plain import Style as PlainStyle
from pybtex.plugin import register_plugin

### BIBTEX EXPERIMENT - SORT SOME BIBLIOGRAPHIES BY TITLE
# 1. Define the custom sorting logic
class TitleSorter(BaseSortingStyle):
    def sorting_key(self, entry):
        # Fetch the title. If a citation doesn't have a title (e.g., @misc), 
        # fallback to the citation key so the compiler doesn't crash.
        title = entry.fields.get('title', entry.key)
        
        # Remove any BibTeX curly braces and convert to lowercase 
        # to ensure perfect alphabetical sorting
        clean_title = title.replace('{', '').replace('}', '').lower()
        
        # Pybtex expects a tuple for sorting keys (primary, secondary, etc.)
        return (clean_title, )

# 2. Inherit your preferred visual style and inject the new sorter
class PlainTitleStyle(PlainStyle):
    default_sorting_style = 'title_sorter'

# 3. Register both plugins with pybtex
register_plugin('pybtex.style.sorting', 'title_sorter', TitleSorter)
register_plugin('pybtex.style.formatting', 'plaintitle', PlainTitleStyle)

### 

# Check if this is on ReadTheDocs, which sets a specific environment variable
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = ['sphinx.ext.autodoc',
                'myst_parser',
                'sphinx.ext.todo', 
                #'sphinx.ext.imgmath', 
                'sphinx.ext.mathjax', 
                'sphinx.ext.graphviz', 
                'sphinxcontrib.bibtex', 
                'sphinxcontrib.mermaid', 
                'sphinxcontrib.sqltable',
                'nbsphinx',
                'sphinx_design',
                'sphinx_copybutton',
                'sphinx_togglebutton']

# BIBTEXT

bibtex_bibfiles = ['./_sharedFiles/cis_guidance_documents.bib',
                   './_sharedFiles/wise_gis_guidance.bib',
                   './_sharedFiles/wfd_reporting_guidance.bib',
                   './_sharedFiles/sdmx_documents.bib',
                   './_sharedFiles/inspire_technical_guidance.bib',
                   './_sharedFiles/eu_legislation.bib']
bibtex_reference_style = 'author_year'



templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','*.txt']

# NUMBERING
# The separator must defined in a custom.css :-(
numfig = True
numfig_format = {
    'figure': 'Figure %s',       # Changes "Fig. 1" to "Figure 1"
    'table': 'Table %s',    
    'code-block': 'Example %s',  # Changes "Listing 1" to "Example 1"
    'section': 'Section %s',     
}

# -- Sphinx-copybutton options ---------------------------------------------
# Exclude copy button from appearing over notebook cell numbers by using :not()
# The default copybutton selector is `div.highlight pre`
# https://github.com/executablebooks/sphinx-copybutton/blob/master/sphinx_copybutton/__init__.py#L82
copybutton_exclude = ".linenos, .gp"
copybutton_selector = ":not(.prompt) > div.highlight pre"

# MERMAID DIAGRAMS 
mermaid_init_js = """
mermaid.initialize({theme:"neutral"});
"""

# SYNTAX HIGHLIGHTING - The name of the Pygments style to use.
pygments_style = 'sphinx'

# Support for todo items: 
# If todo_include_todos = True, todo and todolist produce output, else they produce nothing. The default is False.
todo_include_todos = True
# If todo_link_only = True, todolist produce output without file path and line.
todo_link_only = True

# MATH - Tell MyST to allow dollar signs and advanced math blocks
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "colon_fence",
    "linkify",
    "attrs_inline"
]

# SQLTABLE - configure the default connection if there is one
#sqltable_connection_string = ''

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'pydata_sphinx_theme'
html_show_copyright = False
# The _static folder is where you place files that should be copied as-is to your final build output (_build/html/_static). It is commonly used for:
# Custom.css: To override the default theme colors or fonts.
# Logos/Favicons: Images referenced directly in your theme configuration.
# JavaScript: Scripts for custom interactivity not provided by extensions.
html_static_path = ['_static']
html_css_files = [
   'customTable.css',
   'customTheme.css'
]
html_sidebars = {
    "**": ["sidebar-collapse", "sidebar-nav-bs"],
    "**/index.md": [],
}

html_js_files = [
    "js/mermaid-zoom.js",
]

html_theme_options = {
    "logo": {
        "alt_text": "WISE WFD Documentation",
        "text": "Water Framework Directive",
    },
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
    "show_toc_level": 3, 
    "use_edit_page_button": True,
    "navbar_align": "right"
}

html_sidebars = {
  "**/index.md": []
}

html_context = {
    "github_user": "eeadata",
    "github_repo": "WISE.WFD.Documentation",
    "github_version": "main",
    "doc_path": "docs",
}
html_logo = "_static/wise.svg"

# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'WISE.WFD.Documentation'
copyright = '2025-2026'
author = 'WISEr team'
version = '0.1'

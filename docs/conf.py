# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os

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

bibtex_bibfiles = ['./_sharedFiles/Bibliography.bib']

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
   'customTable.css'
]
html_sidebars = {
    "**": ["sidebar-collapse", "sidebar-nav-bs"]
}

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

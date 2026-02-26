# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os

# Check if this is on ReadTheDocs, which sets a specific environment variable
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

if on_rtd:
   extensions = ['sphinx.ext.autodoc',
                 'myst_parser',
                 'sphinx.ext.todo', 
                 'sphinx.ext.imgmath', 
                 'sphinx.ext.mathjax', 
                 'sphinx.ext.graphviz']
else:
   extensions = ['sphinx.ext.autodoc',
                 'myst_parser',
                 'sphinx.ext.todo', 
                 'sphinx.ext.imgmath', 
                 'sphinx.ext.mathjax', 
                 'sphinx.ext.graphviz', 
                 'sphinxcontrib.bibtex', 
                 'sphinxcontrib.mermaid', 
                 'sphinxcontrib.xlsxtable']
	

bibtex_bibfiles = ['./_sharedFiles/Bibliography.bib']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','*.txt']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Support for todo items: If this is True, todo and todolist produce output, else they produce nothing. The default is False.
todo_include_todos = True

# To be checked: The imgmath_latex variable specifies the LaTeX command to use for rendering math in the imgmath extension. 
# The default is 'latex', which uses the standard LaTeX command.
# You can customize this if you want to use a different command or if you have specific requirements for your math rendering.
imgmath_latex = 'latex'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_show_copyright = False
# The _static folder is where you place files that should be copied as-is to your final build output (_build/html/_static). It is commonly used for:
# Custom.css: To override the default theme colors or fonts.
# Logos/Favicons: Images referenced directly in your theme configuration.
# JavaScript: Scripts for custom interactivity not provided by extensions.
html_static_path = ['_static']

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'WISE.Documentation'
copyright = '2013-2026. These pages aggregate content from multiple sources (refer to the metadata).'
author = 'Fernanda Nery'
version = '0.1'
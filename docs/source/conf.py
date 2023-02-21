# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sys
import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'smart energy simulator'
copyright = '2023, mleist'
author = 'mleist'
github_ref_name = os.getenv("GITHUB_REF_NAME", "--")


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


sys.path.insert(0, os.path.abspath('../../src'))
sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinxcontrib.plantuml',
    'sphinx.ext.autosummary',
    'sphinx_click',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_show_copyright = False
html_show_sphinx = False
html_logo = "_static/se-di-small.png"
html_favicon = '_static/se-di-blue-ball.png'

templates_path = ['_templates']

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'style_external_links': False,
}
html_context = {'my_github_ref_name': github_ref_name}

autosummary_generate = True  # Turn on sphinx.ext.autosummary

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

myst_heading_anchors = 2
myst_enable_extensions = [
    "colon_fence",
    "substitution",
]
suppress_warnings = ["myst.header"]

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration
todo_include_todos = True

today_fmt = '%Y-%m-%dT%H:%M:%S%z'

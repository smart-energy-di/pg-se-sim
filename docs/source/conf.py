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
    'sphinx_multiversion',
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

# ----- Options sphinx-multiversion ------------------------------------------

# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = r'^.*$'

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = r'^.*$'

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = None

# Pattern for released versions
# smv_released_pattern = r'^tags/.*$'           # Tags only
# smv_released_pattern = r'^heads/\d+\.\d+$'    # Branches like "2.1"
# smv_released_pattern = r'^(tags/.*|heads/\d+\.\d+)$'           # Branches like "2.1" and all tags
# smv_released_pattern = r'^(heads|remotes/[^/]+)/(?!:main).*$'  # Everything except main branch


# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'

# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
smv_prefer_remote_refs = False

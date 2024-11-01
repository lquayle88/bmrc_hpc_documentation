# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'BMRC HPC Documentation'
copyright = '2024, Dr Lewis A Quayle'
author = 'Dr Lewis A Quayle'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = []
# html_static_path = ['_static']

# GitHub integration
html_context = {
    "display_github": True,
    "github_user": "lquayle88",
    "github_repo": "bmrc_hpc_documentation",
    "github_version": "main",
    "conf_py_path": "/",
}

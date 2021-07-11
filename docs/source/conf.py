# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

import ez_sphinx

sys.path.insert(0, os.path.abspath('../..'))
print(sys.path)

# -- Project information -----------------------------------------------------

project = 'hello'
copyright = '2021, Yawei Li'
author = 'Yawei Li'

# The full version, including alpha/beta/rc tags
version = ez_sphinx.version
release = ez_sphinx.version

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'recommonmark',
    'sphinx.ext.autosectionlabel',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

language = 'en'

exclude_patterns = []

pygments_style = "sphinx"

add_module_names = False

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'collapse_navigation': False,
    'display_version': True,
    'logo_only': True,
    'navigation_depth': 2,
}

master_doc = "index"

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Configuration file for the Sphinx documentation builder.

import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------

project = "vision-aid"
author = "TheDomSoft"
current_year = datetime.now().year
copyright = f"{current_year}, {author}"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",  # Allow Markdown via MyST
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Google/NumPy docstrings
    "sphinx.ext.viewcode",
]

# Source parsing
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# If you later add a package to autodoc, ensure it's importable here, e.g.:
# sys.path.insert(0, os.path.abspath(".."))

# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
# Add any custom paths here
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = 'Netflix TV Setup Guide'
copyright = '2025, Netflix'
author = 'Netflix Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = []

# Paths to custom templates and static files
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------
# Title shown in the browser tab and top of HTML pages
html_title = "How to Set Up and Enjoy Netflix on Your TV – netflix.com/tv2"

# Short title (e.g., for navigation)
html_short_title = "Netflix TV2 Setup"

# Favicon (make sure you have a favicon.ico in your root or _static directory)
html_favicon = 'favicon.ico'

# Theme (enable one if you have it installed, or leave commented)
html_theme = 'sphinx_rtd_theme'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Enable raw HTML if using embedded HTML in .rst
raw_enabled = True

# Static path for styles, JS, or images (if needed)
# html_static_path = ['_static']

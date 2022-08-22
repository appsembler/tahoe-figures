"""Set up for the Tahoe Figures Customizations package."""

from setuptools import setup

description = 'Backends and customizations for Figures in Tahoe.'

setup(
    name='tahoe-figures-plugins',
    version='0.1.1',
    description=description,
    long_description=description,
    long_description_content_type="text/markdown",
    packages=[
        'tahoe_figures_plugins',
    ],
)

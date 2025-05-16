from setuptools import setup, find_packages

INSTALL_REQUIRES = ["intake >=0.6.6", "pandas", "numpy", "requests"]

setup(
    name="tethysdash_plugin-great_lakes_viewer",
    version="0.0.1",
    description="Great Lakes visualization plugins for tethysdash",
    url="https://github.com/FIRO-Tethys/tethysdash_plugin_geoglows",
    maintainer="Yue Sun",
    maintainer_email="ysun@aquaveo.com",
    license="BSD",
    py_modules=["tethysdash_plugin-great_lakes_viewer"],
    packages=find_packages(),
    entry_points={
        "intake.drivers": [
            "great_lakes_plots = visualizations.plots:Plots",
            "usgs_map = visualizations.map:Map",
        ]
    },
    package_data={"": ["*.csv", "*.yml", "*.html"]},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)

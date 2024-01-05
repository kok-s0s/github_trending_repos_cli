from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="github-trending-repos",
    version="1.1.0",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="A CLI tool for retrieving trending GitHub repositories.",
    install_requires=[
        "beautifulsoup4==4.12.2",
        "PyTermGUI==7.7.0",
        "requests==2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "github-trending-repos = src.gtr:main",
        ],
    },
)

import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="abbreviation_search",
    version="1.0.0",
    author="Andrii Boichuk, Bohdan Domnenko",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fitz109/abbreviation_search",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.6"
)
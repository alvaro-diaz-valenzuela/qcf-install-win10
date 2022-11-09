import setuptools
import sys

print(sys.version_info[0:2])

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qc_financial",
    version="0.1.3",
    author="Alvaro Díaz",
    author_email="alvaro@efaa.cl",
    description="Valuation of linear FX and Interest Rate Derivatives",
    long_description=long_description,
    include_package_data=True,
    long_description_content_type="text/markdown",
    url="https://github.com/adiaz-efaa/qcf-install-win10.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    packages=setuptools.find_packages(),
)

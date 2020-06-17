from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="megatools",
    version="0.0.1",
    author="Harkame",
    description="Megatools's wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Harkame/Megatools",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
)

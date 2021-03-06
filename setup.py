import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="custom-plotting-lcdunne",  # Replace with your own username
    version="0.0.1",
    author="Lewis Dunne",
    author_email="",
    description="A small package for custom plots.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lcdunne/custom_plotting",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

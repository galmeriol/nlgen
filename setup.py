import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nlgen",
    version="0.0.1",
    author="galmeriol",
    author_email="zzafererdogann@gmail.com",
    description="MJML newsletter generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/galmeriol/nlgen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
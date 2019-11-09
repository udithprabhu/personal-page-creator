import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="personal-page-creator",
    version="0.0.1",
    author="Udith Prabhu",
    author_email="udithprabhu@gmail.com",
    description="Script to generate static page for GitHub pages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/udithprabhu/personal-page-creator",
    packages=setuptools.find_packages(),
    scripts=['personal-page-creator'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
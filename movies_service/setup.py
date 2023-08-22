import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="movies_service",
    version="0.0.1",
    author="Jamie Omondi",
    author_email="cruiseomondi90@gmail.com",
    description="Movies Service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[],
)
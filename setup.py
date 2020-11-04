import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aioradios", 
    version="0.0.1",
    author="Peach",
    author_email="ariechertkov@gmail.com",
    description="An asynchronous API wrapper for www.radio-browser.info",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/P3qch/aioradios",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
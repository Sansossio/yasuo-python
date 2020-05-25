import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yasuo", # Replace with your own username
    version="0.1.0",
    author="Julio Sansossio",
    author_email="juliosansossio@gmail.com",
    description="Riot games api wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sansossio/yasuo",
    packages=setuptools.find_packages(),
    keywords=["LoL", "League of Legends", "Riot Games", "API", "yasuo", "wrapper"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

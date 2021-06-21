import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="afib",
    version="0.0.1",
    author="Joyce Ho",
    author_email="joyce.c.ho@emory.edu",
    description="Scores for AFIB",
    url="https://github.com/joyceho/afib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
                      'numpy',
                      'pytest'
                      ],
    zip_safe=False
)
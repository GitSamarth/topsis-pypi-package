from setuptools import setup, find_packages

setup(
    name="Topsis-Samarth-102303717", 
    version="1.0.0",
    author="Samarth Mahajan",
    description="TOPSIS implementation using Python",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis_samarth.topsis:main"
        ]
    },
)


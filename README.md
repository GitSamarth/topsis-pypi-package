# topsis-pypi-package
---

## 📚 Learn How to Build Your First PyPI Package

This project is also intended as a **reference implementation** for students and beginners who want to learn how to create and publish their first Python package on PyPI.

### Step 1: Use the Package
First, install and use this package from PyPI to understand how a real-world Python package works:

```bash
pip install Topsis-Samarth-102303717
```
Run it from the command line:
```bash
topsis data.csv "1,1,1,1,1" "+,+,+,+,+" result.csv
```
Observe:
Command-line interface
Argument handling
Output generation

Step 2: Explore the Repository Structure
This repository demonstrates a standard PyPI-compatible structure:

topsis-cli-pypi/
├── topsis_samarth/
│   ├── __init__.py
│   └── topsis.py
├── setup.py
├── README.md
├── LICENSE
└── requirements.txt


setup.py: package metadata and entry points
Package folder (topsis_samarth/): core logic
LICENSE: open-source licensing

Step 3: Build Your Own Package
You can use this repository as a template to build your own PyPI package:
Replace the algorithm logic with your own code
Rename the package folder
Update setup.py with your details
Write a clear README

Build the package:
```bash
python setup.py sdist bdist_wheel
```
Upload to PyPI using twine

This project demonstrates the complete lifecycle of a Python package:
development → packaging → publishing → usage

Step 4: Extend Further
After building a basic package, you can:
Add validation and error handling
Improve CLI usability
Add tests
Publish new versions on PyPI

🎯 Learning Objective
The goal of this project is not only to provide a working TOPSIS implementation,
but also to help beginners understand how real Python packages are built and shared.

👤 Author
Samarth Mahajan
B.Tech Computer Engineering
Thapar Institute of Engineering and Technology

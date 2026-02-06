# Topsis-pypi-package
---

## 📚 Learn How to Build Your First PyPI Package

This project is also intended as a **reference implementation** for students and beginners who want to learn how to create and publish their first Python package on PyPI.

### Use the Package
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

---

## 🔐 Publishing to PyPI (Step-by-Step Guide)

This section explains the basic steps required to create and publish
your first Python package on **PyPI**, using this project as a reference.

---

### Step 1: Create a PyPI Account

1. Go to https://pypi.org/
2. Sign up for a new account
3. Verify your email address
4. Enable two-factor authentication (recommended)

---

### Step 2: Prepare the Project Structure

A Python package must follow a standard folder structure.
This project uses the following PyPI-compatible layout:

```text
topsis-cli-pypi/
├── topsis_samarth/
│   ├── __init__.py
│   └── topsis.py
├── setup.py
├── README.md
├── LICENSE
└── requirements.txt
```


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
Step 3: Install Packaging Tools

Before building the package, install required tools:
```
pip install setuptools wheel twine
```
Step 4: Build the Package
From the project root directory, run:
python setup.py sdist bdist_wheel
This command generates a dist/ folder containing the package files.

Step 5: Upload to PyPI
Upload the package using twine:
```
twine upload dist/*
```
You will be prompted to enter:
PyPI username
PyPI password (or API token)
After successful upload, the package becomes publicly available on PyPI.

Step 6: Verify Installation
Once uploaded, test the package:
```
pip install <your-package-name>
```

Run it from the command line to confirm it works correctly.

This project demonstrates the complete lifecycle of a Python package:
development → packaging → publishing → usage



🎯 Learning Objective
The goal of this project is not only to provide a working TOPSIS implementation,
but also to help beginners understand how real Python packages are built and shared.

👤 Author
Samarth Mahajan
B.Tech Computer Engineering
Thapar Institute of Engineering and Technology

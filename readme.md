# TOPSIS Python Package

This package provides a Python implementation of the TOPSIS  
(Technique for Order Preference by Similarity to Ideal Solution)  
method for multi-criteria decision making.

---

## Installation

Install the package using pip:

```bash
pip install Topsis-Samarth-102303717

usage

```bash
topsis <InputDataFile> <Weights> <Impacts> <OutputFile>

### Example
```bash
topsis data.csv "1,1,1,1,1" "+,+,+,+,+" result.csv

## Input File Format

- Input file must be a CSV file.
- First column contains the names of alternatives.
- Remaining columns must contain numeric values only.
- The input file must contain at least three columns.

```csv
Fund Name,P1,P2,P3,P4,P5
M1,0.67,0.45,6.5,42.6,12.56
M2,0.60,0.36,3.6,53.3,14.47

## Weights and Impacts

- Weights must be numeric and comma-separated.
- Impacts must be either + (benefit) or - (cost).
- Number of weights must be equal to number of impacts.
- Number of weights and impacts must match the number of criteria.

## Output File

- Output file is generated in CSV format.
- Two new columns are added:
  - Topsis Score
  - Rank

## Author

Samarth Mahajan

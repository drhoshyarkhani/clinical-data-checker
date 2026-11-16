# Clinical Data Checker

A beginner Python project for checking patient research data stored in a CSV file.

## Features

- Detects missing patient IDs.
- Flags repeated IDs after their first occurrence.
- Detects missing, non-numeric, and negative ages.
- Saves identified issues to a CSV report.
- Leaves the input file unchanged.

## Input

Place a file named `patients.csv` in the project folder.
It must contain the columns `id` and `age`.

Example using fictional data:

```csv
id,age
p001,58V
p002,-50
p003,
p004,42
```

## How to run

Requires Python 3. No additional packages are needed.

Open a terminal in the project folder and run:

```bash
python3 patient_check.py
```

## Output

The program creates `issues_report.csv` with these columns:

- `row`: record position, counting the header as row 1.
- `patient_id`: the patient identifier.
- `message`: a description of the issue.

Each run replaces the previous report.

## Limitations

This is an educational prototype with basic data checks.

It expects a correctly structured CSV with the required columns.
It does not yet check all invalid numeric values, upper age limits,
dates, or Excel files.

Reported row numbers match file lines when each record occupies
one line and there are no extra blank lines.

Passing these checks does not guarantee that a record is correct.
Flagged issues require human review.

## Sample data

The included patient records are fictional.
Do not upload identifiable patient data to this repository.
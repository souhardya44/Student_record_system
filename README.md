# Student Record Management & Search System

## Objective
The objective of this assignment is to implement a robust **Student Record Management & Search System** in Python using Object-Oriented Programming (OOP) principles, multi-file module architecture, command-line argument parsing, and structured file handling across **TXT, CSV, and JSON** file formats without relying on external libraries like Pandas or NumPy.

## Features
* **Student Data Representation**: Model individual student details including Student ID, Name, Department, Semester, and Marks in 3 subjects.
* **Calculations & Evaluation**: Auto-compute total marks, average percentage, and pass/fail status.
* **Student Records Manager**: Aggregate student objects, add/remove records dynamically.
* **Custom Search Engine**: Basic loop and condition-based search filters (Search by ID, Search by Name, Search by Department, and Condition Search by Minimum Average Marks).
* **Multi-Format File Support**: Read and write capabilities for `.txt`, `.csv`, and `.json` data files.
* **CLI Interface**: Process command-line flags using Python's `argparse` module.

## Project Structure
```text
student-record-system/
│
├── data/
│   ├── students.txt        # Plain text student record file
│   ├── students.csv        # CSV file with header row
│   └── students.json       # JSON array of student objects
│
├── student.py              # Class definition for Student
├── manager.py              # Class definition for StudentManager
├── file_handler.py         # Module for file parsing and dumping (TXT, CSV, JSON)
├── main.py                 # Command line runner and execution coordinator
└── README.md               # Complete documentation

```
## Input and Output

### Input
* Input data files are stored under the `data/` directory (`students.txt`, `students.csv`, `students.json`).
* Dynamic parameters are passed via CLI flags (`--file`, `--format`, `--search-id`, `--search-name`, `--search-dept`, `--min-avg`, `--out`).

### Output
* Execution logs and query results are displayed on the terminal screen.
* Processed outputs for sample command executions have been captured and saved in the [`output/`](./output/) directory:
  * [`output/display_all_output.txt`](./output/display_all_output.txt): Output when displaying all records.
  * [`output/search_by_id_output.txt`](./output/search_by_id_output.txt): Output when searching by Student ID.
  * [`output/search_by_name_output.txt`](./output/search_by_name_output.txt): Output when searching by Name.
  * [`output/search_by_dept_output.txt`](./output/search_by_dept_output.txt): Output when searching by Department.
  * [`output/condition_search_output.txt`](./output/condition_search_output.txt): Output when filtering by average marks.

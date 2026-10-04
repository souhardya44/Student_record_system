"""
main.py
CLI Interface and main execution flow using argparse.
"""

import argparse
from manager import StudentManager
from file_handler import FileHandler
from student import Student

def main():
    parser = argparse.ArgumentParser(description="Student Record Management & Search System")
    parser.add_argument("--file", required=True, help="Path to input data file (e.g. data/students.csv)")
    parser.add_argument("--format", required=True, choices=["txt", "csv", "json"], help="File format: txt, csv, or json")
    parser.add_argument("--out", help="Path to save updated file (optional)")
    
    # Optional action arguments for quick CLI operations
    parser.add_argument("--search-id", type=int, help="Search student by ID")
    parser.add_argument("--search-name", help="Search student by Name")
    parser.add_argument("--search-dept", help="Search student by Department")
    parser.add_argument("--min-avg", type=float, help="Filter students with average >= min_avg")
    
    args = parser.parse_args()

    manager = StudentManager()

    # Load records based on format
    fmt = args.format.lower()
    if fmt == "txt":
        loaded = FileHandler.read_txt(args.file)
    elif fmt == "csv":
        loaded = FileHandler.read_csv(args.file)
    elif fmt == "json":
        loaded = FileHandler.read_json(args.file)

    for s in loaded:
        manager.add_student(s)

    print("=" * 80)
    print(f" Loaded {len(manager.students)} records from {args.file} ({fmt.upper()} format)")
    print("=" * 80)

    # Perform command line filtering actions if provided
    if args.search_id:
        print(f"\n--- Searching for ID: {args.search_id} ---")
        res = manager.search_by_id(args.search_id)
        if res:
            print(res.display_student())
        else:
            print("Student not found.")

    elif args.search_name:
        print(f"\n--- Searching for Name containing: '{args.search_name}' ---")
        results = manager.search_by_name(args.search_name)
        for r in results:
            print(r.display_student())

    elif args.search_dept:
        print(f"\n--- Searching for Department: '{args.search_dept}' ---")
        results = manager.search_by_department(args.search_dept)
        for r in results:
            print(r.display_student())

    elif args.min_avg is not None:
        print(f"\n--- Students with Average Marks >= {args.min_avg} ---")
        results = manager.search_by_average(args.min_avg)
        for r in results:
            print(r.display_student())

    else:
        # Default view: Display all records
        print("\n--- All Student Records ---")
        manager.display_all_students()

    # Save output if specified
    if args.out:
        if fmt == "txt":
            FileHandler.write_txt(args.out, manager.students)
        elif fmt == "csv":
            FileHandler.write_csv(args.out, manager.students)
        elif fmt == "json":
            FileHandler.write_json(args.out, manager.students)
        print(f"\n Saved updated data to: {args.out}")

if __name__ == "__main__":
    main()
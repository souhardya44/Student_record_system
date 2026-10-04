"""
file_handler.py
Module responsible for reading and writing data across TXT, CSV, and JSON files.
"""

import csv
import json
from student import Student

class FileHandler:
    @staticmethod
    def read_txt(filepath):
        """Reads plain TXT file and returns list of Student objects."""
        students = []
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(',')]
                if len(parts) >= 7:
                    s_id = parts[0]
                    name = parts[1]
                    dept = parts[2]
                    sem = parts[3]
                    marks = [parts[4], parts[5], parts[6]]
                    students.append(Student(s_id, name, dept, sem, marks))
        return students

    @staticmethod
    def write_txt(filepath, students):
        """Writes list of Student objects to a plain TXT file."""
        with open(filepath, 'w') as file:
            for s in students:
                m_str = ", ".join([str(m) for m in s.marks])
                line = f"{s.student_id}, {s.name}, {s.department}, {s.semester}, {m_str}\n"
                file.write(line)

    @staticmethod
    def read_csv(filepath):
        """Reads CSV file using Python csv library and returns list of Student objects."""
        students = []
        with open(filepath, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)  # Skip header
            for row in reader:
                if row:
                    s_id, name, dept, sem = row[0], row[1], row[2], row[3]
                    marks = [row[4], row[5], row[6]]
                    students.append(Student(s_id, name, dept, sem, marks))
        return students

    @staticmethod
    def write_csv(filepath, students):
        """Writes list of Student objects to CSV file."""
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name", "Department", "Semester", "Subject1", "Subject2", "Subject3"])
            for s in students:
                writer.writerow([s.student_id, s.name, s.department, s.semester, s.marks[0], s.marks[1], s.marks[2]])

    @staticmethod
    def read_json(filepath):
        """Reads JSON file using python json library and returns list of Student objects."""
        students = []
        with open(filepath, 'r') as file:
            data = json.load(file)
            for item in data:
                s_id = item["student_id"]
                name = item["name"]
                dept = item["department"]
                sem = item["semester"]
                marks_dict = item["marks"]
                marks = [marks_dict["subject1"], marks_dict["subject2"], marks_dict["subject3"]]
                students.append(Student(s_id, name, dept, sem, marks))
        return students

    @staticmethod
    def write_json(filepath, students):
        """Writes list of Student objects to JSON file."""
        data = []
        for s in students:
            data.append({
                "student_id": s.student_id,
                "name": s.name,
                "department": s.department,
                "semester": s.semester,
                "marks": {
                    "subject1": s.marks[0],
                    "subject2": s.marks[1],
                    "subject3": s.marks[2]
                }
            })
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=2)
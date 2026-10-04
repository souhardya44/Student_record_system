"""
manager.py
Contains the StudentManager class responsible for holding multiple Student objects
and performing basic loop/condition-based operations.
"""

from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        # Adds a Student object to the list
        self.students.append(student)

    def remove_student(self, student_id):
        # Removes student by ID using loop and comparison
        target_index = -1
        for i in range(len(self.students)):
            if self.students[i].student_id == int(student_id):
                target_index = i
                break
        if target_index != -1:
            del self.students[target_index]
            return True
        return False

    def search_by_id(self, student_id):
        # Search student by exact ID.
        for s in self.students:
            if s.student_id == int(student_id):
                return s
        return None

    def search_by_name(self, name):
        """Search students by name match (case-insensitive substring)."""
        results = []
        for s in self.students:
            if name.lower() in s.name.lower():
                results.append(s)
        return results

    def search_by_department(self, dept):
        """Search students by department match."""
        results = []
        for s in self.students:
            if dept.lower() in s.department.lower():
                results.append(s)
        return results

    def search_by_average(self, min_avg):
        """Finds students whose average score is greater than or equal to min_avg."""
        results = []
        for s in self.students:
            if s.calculate_average() >= float(min_avg):
                results.append(s)
        return results

    def display_all_students(self):
        """Prints all student details."""
        if not self.students:
            print("No student records available.")
            return
        for s in self.students:
            print(s.display_student())
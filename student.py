"""
student.py
Contains the Student class representing individual student entity and operations.
"""

class Student:
    def __init__(self, student_id, name, department, semester, marks):
        self.student_id = int(student_id)
        self.name = str(name).strip()
        self.department = str(department).strip()
        self.semester = int(semester)
        # marks is expected as a list of integers [subject1, subject2, subject3]
        self.marks = [int(m) for m in marks]

    def calculate_total(self):
        """Calculates total marks across all 3 subjects."""
        total = 0
        for m in self.marks:
            total += m
        return total

    def calculate_average(self):
        """Calculates average marks of the student."""
        if len(self.marks) == 0:
            return 0.0
        return self.calculate_total() / len(self.marks)

    def get_result(self):
        """Determines pass/fail status based on passing criteria (>40 per subject)."""
        for m in self.marks:
            if m < 40:
                return "Fail"
        return "Pass"

    def update_marks(self, new_marks):
        """Updates subject marks."""
        if len(new_marks) == 3:
            self.marks = [int(m) for m in new_marks]
            return True
        return False

    def display_student(self):
        """Returns formatted string output of student details."""
        avg = self.calculate_average()
        tot = self.calculate_total()
        res = self.get_result()
        return (f"ID: {self.student_id} | Name: {self.name:<10} | Dept: {self.department:<18} | "
                f"Sem: {self.semester} | Marks: {self.marks} | Total: {tot} | Avg: {avg:.2f} | Status: {res}")
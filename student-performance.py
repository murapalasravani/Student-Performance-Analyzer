
# Student Performance Analyzer
# A beginner-friendly Python and DSA project

PASS_MARK = 35

students = [
    {"name": "Anu", "marks": [85, 90, 80]},
    {"name": "Ravi", "marks": [60, 55, 65]},
    {"name": "Priya", "marks": [95, 92, 98]},
    {"name": "Kiran", "marks": [35, 40, 30]},
    {"name": "Sneha", "marks": [75, 80, 85]}
]


def analyze_students(students):
    """Calculate total, average, and pass/fail status."""

    for student in students:
        marks = student["marks"]

        student["total"] = sum(marks)
        student["average"] = student["total"] / len(marks)

        if all(mark >= PASS_MARK for mark in marks):
            student["result"] = "Pass"
        else:
            student["result"] = "Fail"


def display_report(students):
    """Display the student performance report."""

    print("\nSTUDENT PERFORMANCE REPORT")
    print("-" * 65)
    print(f"{'Name':<12}{'Total':<10}{'Average':<12}{'Result':<10}")  #creating a header <leftside 12characters
    print("-" * 65)

    for student in students:
        print(
            f"{student['name']:<12}"
            f"{student['total']:<10}"
            f"{student['average']:<12.2f}"
            f"{student['result']:<10}"
        )


def rank_students(students):
    """Sort students by average marks, highest first."""

    students.sort(
        key=lambda student: student["average"],
        reverse=True
    )


def display_topper(students):
    """Display the student with the highest average."""

    if students:
        print(f"\nClass Topper: {students[0]['name']}")
        print(f"Average Marks: {students[0]['average']:.2f}")


def search_student(students, name):
    """Search for a student by name."""

    for student in students:
        if student["name"].casefold() == name.strip().casefold():
            return student

    return None


def main():
    analyze_students(students)
    rank_students(students)
    display_report(students)
    display_topper(students)

    name = input("\nEnter a student name to search: ")
    student = search_student(students, name)

    if student:
        print("\nStudent Found")
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Total: {student['total']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Result: {student['result']}")
    else:
        print("Student not found.")


if __name__ == "__main__":
    main()

# Student Performance Analyzer

A beginner-friendly Python project that analyzes student marks, calculates academic performance, ranks students, and searches for individual student records.

## Features

- Calculate total and average marks
- Determine pass or fail status
- Rank students by average marks
- Identify the class topper
- Search for students by name
- Display a formatted performance report
- Understand time and space complexity

## Technologies Used

- Python
- Data Structures: Lists and Dictionaries
- Algorithms: Linear Search and Sorting
- Python sorting: TimSort

## Project Structure

```text
student-performance-analyzer/
├── student-performance.py
├── README.md
└── .gitignore
```

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Run the following command:

```bash
python student-performance.py
```

5. Enter a student name when prompted to search for a record.

## Sample Data

The project uses sample student records with three subject marks per student.

## Complexity Analysis

Let `n` be the number of students and `m` be the number of subjects per student.

| Operation | Time Complexity |
|---|---|
| Analyze student marks | O(nm) |
| Sort students | O(n log n) worst case |
| Display report | O(n) |
| Identify topper after sorting | O(1) |
| Search by name | O(n) worst case |

Overall worst-case time complexity: **O(nm + n log n)**.

Auxiliary space complexity: **O(n)** worst case, excluding the input records.

## Learning Outcomes

- Practised Python functions, loops, conditions, lists, and dictionaries.
- Implemented linear search and sorting.
- Learned how to analyze time and space complexity.
- Practised organizing and documenting a Python project.

## Future Improvements

- Read student data from a CSV file using Pandas.
- Add charts to visualize student performance.
- Export reports to CSV.
- Add input validation and automated tests.

## Author

Created as a Python and Data Structures and Algorithms learning project.


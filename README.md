📊 Student Performance Analyzer

A simple yet powerful Python project that reads student marks from a CSV file, processes the data, calculates totals, averages, and grades, and generates a clean final report.

🚀 Features

Reads student data from a CSV file

Computes:

Total marks

Average marks

Grade based on performance

Generates a clean, readable text report

Beginner-friendly and industry-standard code structure

Perfect mini-project for learning Python + File Handling + Data Processing

📁 Project Structure
student-performance-analyzer/
│
├── data_report_generator.py     # Main Python script
├── students_report.csv          # Input data file
├── final_report.txt             # Auto-generated output report
└── README.md                    # Project documentation

🧠 How It Works

The Python script reads students_report.csv

For each student, it calculates:

Total = sum of all subjects

Average = total / 3

Grade (A+, A, B+, B, etc.)

The results are written into final_report.txt in a clean format

🏷️ Grade Calculation Logic
Average Score	Grade
90–100	A+
80–89	A
70–79	B+
60–69	B
Below 60	C
🖥️ Running the Project
1️⃣ Install Python

Python 3.8+ is recommended.

2️⃣ Run the script
python3 data_report_generator.py


This will generate:

final_report.txt

📝 Sample Output (final_report.txt)
STUDENT PERFORMANCE REPORT
----------------------------
Name: Sree
Total Marks: 262
Average: 87.33
Grade: A

Name: Ananya
Total Marks: 228
Average: 76.00
Grade: B+

🔥 Why This Project Matters

Shows understanding of Python basics

Demonstrates file handling, data processing, and logic building

Adds credibility to your portfolio

Great starting point for more advanced projects

🌟 Future Enhancements

You can extend this project by adding:

Data visualization (Matplotlib)

Exporting final report as PDF

Web interface using Flask or Django

Database storage (SQLite/PostgreSQL)

Emailing the report automatically

🧑‍💻 Author

Sree Ranganath Chippala

📊 Student Performance Analyzer

A Python-powered automated student evaluation engine that processes raw score data, computes totals and averages, assigns grades, and generates clean, structured reports — a foundational project for data processing, AI pipelines, and automation systems.

🚀 Overview

The Student Performance Analyzer reads structured student data from a CSV file and applies an evaluation pipeline that:

🔢 Calculates total marks

📈 Computes average scores

🏷️ Assigns grades based on performance

📄 Produces a clean final_report.txt

This project demonstrates Python file handling, data processing, modular design, and clear report generation — essential skills for data engineers and AI/ML developers.

🧩 Features

| Feature                      | Description                                      |
| ---------------------------- | ------------------------------------------------ |
| 📥 CSV Input Handling        | Reads student records from a structured CSV file |
| 🧮 Automatic Calculations    | Computes total & average marks                   |
| 🏷️ Grade Assignment Engine  | Assigns A+, A, B+, B, C                          |
| 📄 Report Generation         | Outputs a clean, readable text report            |
| 🧱 Simple, Extensible Design | Easily expandable to ML/analytics use-cases      |


📁 Project Structure

student-performance-analyzer/
│
├── data_report_generator.py   # Core script - processing and report generation
├── students_report.csv        # Input dataset
├── final_report.txt           # Auto-generated output report
└── README.md                  # Documentation (this file)

⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/sreeranga-chippala/student-performance-analyzer.git
cd student-performance-analyzer

2️⃣ Run the Program

python3 data_report_generator.py

A new file final_report.txt will be created with computed results.

🧠 Sample Output

Name: Sree
Total Marks: 262
Average: 87.33
Grade: A

🎓 Grade Criteria

| Average  | Grade |
| -------- | ----- |
| 90–100   | A+    |
| 80–89    | A     |
| 70–79    | B+    |
| 60–69    | B     |
| Below 60 | C     |

🧰 Concepts Demonstrated

| Concept                     | Description                                    |
| --------------------------- | ---------------------------------------------- |
| 📄 **File Handling**        | Reading/writing text and CSV files             |
| 🔢 **Data Processing**      | Computing numeric aggregates                   |
| 🧩 **Modular Logic**        | Clear separation for input, processing, output |
| ⚙️ **Error-Free Execution** | Structured code with simple validation         |
| 📊 **Reporting**            | Clean and readable output formatting           |

🧱 Technologies Used

🐍 Python 3

💻 VS Code

🔗 Git & GitHub

📁 CSV data handling

🧩 Procedural + modular programming

💡 Future Enhancements

📊 Add Matplotlib charts

🧾 Export report as PDF

🧮 Integrate with Pandas

📂 Accept Excel/JSON inputs

🌐 Build a Streamlit/Flask dashboard

☁️ Deploy as an API for student evaluation systems

👨‍💻 Author

Chippala Sree Ranganath
🎓 B.E. in Artificial Intelligence and Machine Learning – MSRIT
🏫 Trained under NxtWave CCBP 4.0 Technologies
🌍 Passionate about AI engineering, clean code, and scalable system design

🔗 GitHub: sreeranga-chippala


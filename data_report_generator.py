import time
import os

class StudentReportGenerator:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def calculate_grade(self, avg):
        if avg >= 90:
            return 'A+'
        elif avg >= 80:
            return 'A'
        elif avg >= 70:
            return 'B+'
        elif avg >= 60:
            return 'B'
        elif avg >= 50:
            return 'C'
        else:
            return 'FAIL'

    def generate_report(self):
        try:
            if not os.path.exists(self.input_file):
                raise FileNotFoundError(f"{self.input_file} not found!")

            with open(self.input_file, 'r') as f:
                next(f)
                with open(self.output_file, 'w') as file:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    file.write("STUDENT PERFORMANCE REPORT\n")
                    file.write(f"Generated on: {timestamp}\n")
                    file.write("----------------------------\n")

                    for line in f:
                        try:
                            name, math, science, english = line.strip().split(',')
                            total = int(math) + int(science) + int(english)
                            avg = total / 3
                            grade = self.calculate_grade(avg)
                            file.write(f"\nName: {name}\n")
                            file.write(f"Total Marks: {total}\n")
                            file.write(f"Average: {avg:.2f}\n")
                            file.write(f"Grade: {grade}\n")
                        except ValueError:
                            file.write(f"\n⚠️ Skipped invalid record: {line.strip()}\n")

                    file.write("\n----------------------------\n✅ Report successfully generated!\n")

            print("✅ Report successfully generated!")

        except FileNotFoundError:
            print("❌ Input file not found!")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        finally:
            print("Operation Completed!")


if __name__ == "__main__":
    generator = StudentReportGenerator('students_report.csv', 'final_report.txt')
    generator.generate_report()

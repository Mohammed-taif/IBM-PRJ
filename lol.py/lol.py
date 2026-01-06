import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import statistics

class StudentReportApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Performance Report Generator")
        self.root.geometry("600x600")
        self.root.configure(bg="#1d2b64")

        self.subjects = ['Maths', 'Science', 'English']
        self.marks = {}

        # Title
        tk.Label(
            self.root,
            text="📘 Student Performance Report Generator",
            font=("Arial", 18, "bold"),
            bg="#1d2b64",
            fg="white"
        ).pack(pady=15)

        # Number of students input
        frame = tk.Frame(self.root, bg="#1d2b64")
        frame.pack()
        tk.Label(frame, text="Enter Number of Students:", bg="#1d2b64", fg="white").grid(row=0, column=0, padx=10)
        self.num_entry = tk.Entry(frame, width=5)
        self.num_entry.grid(row=0, column=1)
        tk.Button(frame, text="Set", command=self.create_input_fields, bg="#49a09d", fg="white").grid(row=0, column=2, padx=10)

        self.entry_frame = tk.Frame(self.root, bg="#1d2b64")
        self.entry_frame.pack(pady=10)

        self.root.mainloop()

    def create_input_fields(self):
        for widget in self.entry_frame.winfo_children():
            widget.destroy()

        try:
            self.num_students = int(self.num_entry.get())
            if self.num_students <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of students!")
            return

        self.entries = []

        # Table Header
        header = ["Name"] + self.subjects
        for col, text in enumerate(header):
            tk.Label(self.entry_frame, text=text, bg="#5f2c82", fg="white", width=10, relief="ridge").grid(row=0, column=col, padx=3, pady=3)

        # Input fields
        for i in range(self.num_students):
            row_entries = []
            for j in range(len(header)):
                e = tk.Entry(self.entry_frame, width=10)
                e.grid(row=i + 1, column=j, padx=3, pady=3)
                row_entries.append(e)
            self.entries.append(row_entries)

        tk.Button(self.root, text="Generate Report", command=self.generate_report, bg="#49a09d", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

    def generate_report(self):
        self.marks = {}

        # Collect data from entries
        for row in self.entries:
            name = row[0].get().strip().upper()
            if not name:
                messagebox.showerror("Error", "Student name cannot be empty!")
                return

            student_marks = []
            try:
                for j in range(1, len(self.subjects) + 1):
                    mark = float(row[j].get())
                    if 0 <= mark <= 100:
                        student_marks.append(mark)
                    else:
                        raise ValueError
            except ValueError:
                messagebox.showerror("Error", f"Invalid marks for {name}. Enter values between 0 and 100.")
                return

            self.marks[name] = student_marks

        self.create_analysis()

    def create_analysis(self):
        subjects = self.subjects
        marks = self.marks

        # Subject averages
        subject_avgs = []
        for i, subject in enumerate(subjects):
            subject_marks = [marks[student][i] for student in marks]
            subject_avgs.append(statistics.mean(subject_marks))

        # Top & low subject
        top_subject = subjects[subject_avgs.index(max(subject_avgs))]
        low_subject = subjects[subject_avgs.index(min(subject_avgs))]

        # Top & weak performer
        student_names = list(marks.keys())
        student_avgs = [statistics.mean(marks[student]) for student in marks]

        top_std = student_names[student_avgs.index(max(student_avgs))]
        low_std = student_names[student_avgs.index(min(student_avgs))]

        # Bar charts
        plt.bar(subjects, subject_avgs, color="skyblue")
        plt.title("Average Marks per Subject")
        plt.ylabel("Average Marks")
        plt.savefig("subject_avg.png")
        plt.close()

        plt.bar(student_names, student_avgs, color="orange")
        plt.title("Average Marks per Student")
        plt.ylabel("Average Marks")
        plt.savefig("student_avg.png")
        plt.close()

        # HTML creation
        student_analysis_html = ""
        for student in marks:
            student_analysis_html += f"""
            <div class="student-box">
                <h3>{student}</h3>
                <ul>
                    <li><b>Scores:</b> {marks[student]}</li>
                    <li><b>Average:</b> {statistics.mean(marks[student]):.2f}</li>
                    <li><b>Median:</b> {statistics.median(marks[student]):.2f}</li>
                    <li><b>Mode:</b> {statistics.mode(marks[student])}</li>
                    <li><b>Standard Deviation:</b> {statistics.stdev(marks[student]):.2f}</li>
                </ul>
            </div>
            """

        overall_html = f"""
        <h2>Overall Analysis</h2>
        <div class="overall-box">
            <ul>
                <li><b>Top Performer:</b> {top_std} (Average {max(student_avgs):.2f})</li>
                <li><b>Weak Performer:</b> {low_std} (Average {min(student_avgs):.2f})</li>
                <li><b>Strongest Subject:</b> {top_subject} (Average {max(subject_avgs):.2f})</li>
                <li><b>Weakest Subject:</b> {low_subject} (Average {min(subject_avgs):.2f})</li>
            </ul>
        </div>
        """

        html_content = f"""
        <html>
        <head>
            <title>Student Performance Report</title>
            <style>
                body {{
                    font-family: 'Poppins', Arial, sans-serif;
                    background: linear-gradient(-45deg, #f8cdda, #1d2b64, #5f2c82, #49a09d);
                    background-size: 400% 400%;
                    animation: gradientBG 12s ease infinite;
                    color: #fff;
                }}
                @keyframes gradientBG {{
                    0% {{ background-position: 0% 50%; }}
                    50% {{ background-position: 100% 50%; }}
                    100% {{ background-position: 0% 50%; }}
                }}
                h1 {{ text-align: center; margin-top: 30px; font-size: 2.5em; text-shadow: 2px 2px 5px #000; }}
                table {{
                    border-collapse: collapse; margin: 30px auto; width: 80%;
                    background: rgba(255, 255, 255, 0.1); border-radius: 15px; overflow: hidden;
                }}
                th, td {{ padding: 12px; text-align: center; border: 1px solid rgba(255,255,255,0.3); }}
                th {{ background-color: rgba(0, 0, 0, 0.3); color: #ffd700; }}
                tr:nth-child(even) {{ background-color: rgba(255,255,255,0.05); }}
                .student-box {{
                    background: rgba(255,255,255,0.1); margin: 15px 100px; padding: 15px 25px;
                    border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.3);
                }}
                .overall-box {{
                    background: rgba(255,255,255,0.15); margin: 20px 100px; padding: 20px; border-radius: 15px;
                }}
                img {{ display: block; margin: 25px auto; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.5); }}
                footer {{ text-align: center; margin: 30px; font-weight: bold; color: #ffcccb; }}
            </style>
        </head>
        <body>
            <h1>Student Performance Report</h1>
            <h2 style="text-align:center;">Marks Table</h2>
            <table>
                <tr><th>Student</th>{''.join(f'<th>{s}</th>' for s in self.subjects)}</tr>
                {''.join(f"<tr><td>{st}</td>{''.join(f'<td>{m}</td>' for m in marks[st])}</tr>" for st in marks)}
            </table>

            <h2 style="text-align:center;">Student Analysis</h2>
            {student_analysis_html}
            {overall_html}
            <h2 style="text-align:center;">Graphs</h2>
            <img src="subject_avg.png" width="400">
            <img src="student_avg.png" width="400">
            <footer>By: Mohammed Taif, Midhun, Azman</footer>
        </body>
        </html>
        """

        with open("report.html", "w") as f:
            f.write(html_content)

        messagebox.showinfo("Success", "Report generated successfully! Open 'report.html' to view it.")

# Run app
StudentReportApp()

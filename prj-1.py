import matplotlib.pyplot as plt
import statistics

subjects=['Maths','Science','English']
marks={
    'A':[90,86,70],
    'B':[64,30,50],
    'C':[60,80,90]
}
print(marks)
print('\n')
print("AVERAGE MARKS OF EACH SUBJECTS :\n")
for i, subject in enumerate(subjects):
    subject_marks = [marks[student][i] for student in marks]
    avg = statistics.mean(subject_marks)
    print(f"{subject}: {avg:.2f}")
print("\n")

top_avg=0
top_subject=None
for i, subject in enumerate(subjects):
    subject_marks = [marks[student][i] for student in marks]
    avg = statistics.mean(subject_marks)
    if avg>top_avg:
        top_avg=avg
        top_subject=subject
print("SUBJECT WITH HIGHEST AVERAGE :")
print(f"{top_subject} :",top_avg)

print("\n")
low_avg=100
low_subject=None
for i, subject in enumerate(subjects):
    subject_marks = [marks[student][i] for student in marks]
    avg = statistics.mean(subject_marks)
    if avg<low_avg:
        low_avg=avg
        low_subject=subject
print("SUBJECT WITH LOWEST AVERAGE :")
print(f"{low_subject} :",low_avg)
print("\n")

def st_mean(std):
    print(f"MARKS ANALYSIS REPORT OF {std}")
    print("Average :",statistics.mean(marks[std]))
    print("Median :",statistics.median(marks[std]))
    print("Mode :",statistics.mode(marks[std]))
    print("Standard Deviattion :",statistics.stdev(marks[std]))
    print('\n')

print("STUDENT PERFORMANCE ANALYSIS REPORT :\n")
for students in marks:
    st_mean(students)

#TOP PERFORMER AND WEAK PERFORMER
top_avg=0
top_std=None
for students in marks:
    avg=statistics.mean(marks[students])
    if avg>top_avg:
        top_avg=avg
        top_std=students
print(f"TOP PERFORMER :{top_std}\nAVERAGE :{top_avg}")

low_avg=100
low_std=None
for students in marks:
    avg=statistics.mean(marks[students])
    if avg<low_avg:
        low_avg=avg
        low_std=students
print(f"WEAK PERFORMER :{low_std}\nAVERAGE :{low_avg}")

subject_avgs = []
for i, subject in enumerate(subjects):
    subject_marks = [marks[student][i] for student in marks]
    avg = statistics.mean(subject_marks)
    subject_avgs.append(avg)

student_names = list(marks.keys())
student_avgs = [statistics.mean(marks[student]) for student in marks]

# Generating bar charts
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
        <li><b>Top Performer:</b> {top_std} (Average {top_avg:.2f})</li>
        <li><b>Weak Performer:</b> {low_std} (Average {low_avg:.2f})</li>
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
            margin: 0;
            padding: 0;
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

        h1 {{
            text-align: center;
            color: #fff;
            margin-top: 30px;
            font-size: 2.5em;
            text-shadow: 2px 2px 5px #000;
        }}

        table {{
            border-collapse: collapse;
            margin: 30px auto;
            width: 80%;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            overflow: hidden;
        }}

        th, td {{
            padding: 12px;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.3);
        }}

        th {{
            background-color: rgba(0, 0, 0, 0.3);
            color: #ffd700;
        }}

        tr:nth-child(even) {{
            background-color: rgba(255,255,255,0.05);
        }}

        .student-box {{
            background: rgba(255, 255, 255, 0.1);
            margin: 15px 100px;
            padding: 15px 25px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }}

        .student-box h3 {{
            color: #00ffd5;
            text-shadow: 1px 1px 3px black;
        }}

        .student-box ul {{
            list-style-type: none;
            padding-left: 15px;
        }}

        .overall-box {{
            background: rgba(255,255,255,0.15);
            margin: 20px 100px;
            padding: 20px;
            border-radius: 15px;
        }}

        img {{
            display: block;
            margin: 25px auto;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.5);
        }}

        footer {{
            text-align: center;
            margin: 30px;
            font-weight: bold;
            color: #ffcccb;
        }}
    </style>
</head>
<body>
    <h1>Student Performance Report</h1>

    <h2 style="text-align:center;">Marks Table</h2>
    <table>
        <tr>
            <th>Student</th>
            {''.join(f'<th>{s}</th>' for s in subjects)}
        </tr>
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

print("Report generated: report.html kindly check your browser to view it.")

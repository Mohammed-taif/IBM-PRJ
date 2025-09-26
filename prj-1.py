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
#THIS BLOCK OF CODE FINDS THE AVERAGE MARKS OF EACH SUBJECT
for i, subject in enumerate(subjects):
    subject_marks = [marks[student][i] for student in marks]
    avg = statistics.mean(subject_marks)
    print(f"{subject}: {avg:.2f}")
print("\n")
#THIS BLOCK OF CODE FINDS THE SUBJECT WITH HIGHEST AND LOWEST AVERAGE
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
#THIS BLOCK OF CODE FINDS THE AVERAGE, MEDIAN, MODE AND STANDARD DE
def st_mean(std):
    print(f"MARKS ANALYSIS REPORT OF {std}")
    print("Average :",statistics.mean(marks[std]))
    print("Median :",statistics.median(marks[std]))
    print("Mode :",statistics.mode(marks[std]))
    print("Standard Deviattion :",statistics.stdev(marks[std]))
    print('\n')

#THIS BLOCK OF CODE PRINTS THE STUDENT PERFORMANCE ANALYSIS REPORT
print("STUDENT PERFORMANCE ANALYSIS REPORT :\n")
for students in marks:
    st_mean(students)
#THIS BLOCK OF CODE FINDS THE TOP PERFORMER
top_avg=0
top_std=None
for students in marks:
    avg=statistics.mean(marks[students])
    if avg>top_avg:
        top_avg=avg
        top_std=students
print(f"TOP PERFORMER :{top_std}\nAVERAGE :{top_avg}")

#THIS BLOCK OF CODE FINDS THE WEAK PERFORMER
low_avg=100
low_std=None
for students in marks:
    avg=statistics.mean(marks[students])
    if avg<low_avg:
        low_avg=avg
        low_std=students
print(f"WEAK PERFORMER :{low_std}\nAVERAGE :{low_avg}")
subject_avgs = []

# Calculate average marks for each subject
for i, subject in enumerate(subjects):
    subject_marks = [marks[student][i] for student in marks]
    avg = statistics.mean(subject_marks)
    subject_avgs.append(avg)

# Prepare data for graphs
student_names = list(marks.keys())
student_avgs = [statistics.mean(marks[student]) for student in marks]

# Save graphs instead of showing
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

# DISPLAYING THE FULL REPORT IN HTML FORMAT
student_analysis_html = ""
for student in marks:
    student_analysis_html += f"""
    <h3>{student}</h3>
    <ul>
        <li>Scores: {marks[student]}</li>
        <li>Average: {statistics.mean(marks[student]):.2f}</li>
        <li>Median: {statistics.median(marks[student]):.2f}</li>
        <li>Mode: {statistics.mode(marks[student])}</li>
        <li>Standard Deviation: {statistics.stdev(marks[student]):.2f}</li>
    </ul>
    """

# Build Overall Analysis Section
overall_html = f"""
<h2>Overall Analysis</h2>
<ul>
    <li><b>Top Performer:</b> {top_std} (Average {top_avg:.2f})</li>
    <li><b>Weak Performer:</b> {low_std} (Average {low_avg:.2f})</li>
    <li><b>Strongest Subject:</b> {top_subject} (Average {max(subject_avgs):.2f})</li>
    <li><b>Weakest Subject:</b> {low_subject} (Average {min(subject_avgs):.2f})</li>
</ul>
"""

# Final HTML
html_content = f"""
<html>
<head>
    <title>Student Performance Report</title>
</head>
<body>
    <h1>Performance Report</h1>

    <h2>Marks Table</h2>
    <table border="1" cellpadding="5">
        <tr>
            <th>Student</th>
            {''.join(f'<th>{s}</th>' for s in subjects)}
        </tr>
        {''.join(f"<tr><td>{st}</td>{''.join(f'<td>{m}</td>' for m in marks[st])}</tr>" for st in marks)}
    </table>

    <h2>Student Analysis</h2>
    {student_analysis_html}

    {overall_html}

    <h2>Graphs</h2>
    <img src="subject_avg.png" width="400"><br>
    <img src="student_avg.png" width="400">
</body>
</html>
"""

# Write to HTML file
with open("report.html", "w") as f:
    f.write(html_content)

print("Report generated: report.html kindly check your browser to view it.")

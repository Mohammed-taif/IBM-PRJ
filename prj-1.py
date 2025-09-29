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
  <style>
    body {
      margin: 0;
      height: 100vh;
    
      justify-content: center;
      align-items: center;
      color: white;
      font-family: Arial, sans-serif;
      background: linear-gradient(-45deg, #ff6ec4, #7873f5, #17ead9, #fce38a);
      background-size: 400% 400%;
      animation: gradient 10s ease infinite;
    }
    @keyframes gradient {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
  </style>
</head>
<body bgcolor="lightyellow" text="black">

    <h1 align="center" style="color: darkblue;">Student Performance Report</h1>

    <h2 style="color: darkgreen;">Marks Table</h2>
    <table border="1" cellpadding="5" cellspacing="0" width="70%" align="center" bgcolor="lightcyan">
        <tr bgcolor="red">
            <th>Student</th>
            <th>Maths</th>
            <th>Science</th>
            <th>English</th>
        </tr>
        <tr bgcolor="blue">
            <td>A</td>
            <td>90</td>
            <td>86</td>
            <td>70</td>
        </tr>
        <tr bgcolor="blue">
            <td>B</td>
            <td>64</td>
            <td>30</td>
            <td>50</td>
        </tr>
        <tr bgcolor="blue">
            <td>C</td>
            <td>60</td>
            <td>80</td>
            <td>90</td>
        </tr>
    </table>

    <h2 style="color: darkgreen;">Student Analysis</h2>

    <h3 style="color: purple;">A</h3>
    <ul>
        <li>Scores: 90, 86, 70</li>
        <li>Average: 82</li>
        <li>Median: 86</li>
        <li>Mode: 90</li>
        <li>Standard Deviation: 10.58</li>
    </ul>

    <h3 style="color: purple;">B</h3>
    <ul>
        <li>Scores: 64, 30, 50</li>
        <li>Average: 48</li>
        <li>Median: 50</li>
        <li>Mode: 64</li>
        <li>Standard Deviation: 17.09</li>
    </ul>

    <h3 style="color: purple;">C</h3>
    <ul>
        <li>Scores: 60, 80, 90</li>
        <li>Average: 76.67</li>
        <li>Median: 80</li>
        <li>Mode: 60</li>
        <li>Standard Deviation: 15.28</li>
    </ul>

    <h2 style="color: darkgreen;">Overall Analysis</h2>
    <ul>
        <li><b>Top Performer:</b> A (82)</li>
        <li><b>Weak Performer:</b> B (48)</li>
        <li><b>Strongest Subject:</b> Maths (71.33)</li>
        <li><b>Weakest Subject:</b> Science (65.33)</li>
    </ul>

    <h2 style="color: darkgreen;">Graphs</h2>
    <div align="center">
        <img src="subject_avg.png" width="400"><br><br>
        <img src="student_avg.png" width="400">
    </div>

    <p align="center" style="color: darkred; font-weight:bold;">
        By: Mohammed Taif, Midhun, Azman
    </p>

</body>
</html>

"""

# Write to HTML file
with open("report.html", "w") as f:
    f.write(html_content)

print("Report generated: report.html kindly check your browser to view it.")

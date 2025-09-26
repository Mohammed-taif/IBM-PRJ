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
def st_mean(std):
    print(f"MARKS ANALYSIS REPORT OF {std}")
    print("Average :",statistics.mean(marks[std]))
    print("Median :",statistics.median(marks[std]))
    print("Mode :",statistics.mode(marks[std]))
    print("Standard Deviattion :",statistics.stdev(marks[std]))
    print('\n')

for students in marks:
    st_mean(students)
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

# Bar chart for subject averages
plt.bar(subjects, subject_avgs, color="skyblue")
plt.title("Average Marks per Subject")
plt.ylabel("Average Marks")
plt.show()
student_names = list(marks.keys())
student_avgs = [statistics.mean(marks[student]) for student in marks]

plt.bar(student_names, student_avgs, color="orange")
plt.title("Average Marks per Student")
plt.ylabel("Average Marks")
plt.show()
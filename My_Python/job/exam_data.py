from job_sample_insert import *
reader = all_data()
exam_data = []

for row in reader:
    exam_data.append((row['REF Number'], row['Exam Type'], row['Exam Name'], row['Mean'], row['Standard Deviation'],
                      row['Highest Achievable Score'], row['Lowest Passing Score/Pass Point'],
                      row['Weight of Exam']))
print(exam_data)
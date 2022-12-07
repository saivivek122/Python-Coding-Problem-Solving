from job_sample_insert import *
job_code_title_data = []
exam_data = []
i = 1
reader = all_data()
for row in reader:
    job_code_title_data.append((i,row['Job Code and Title']))
    exam_data.append((row['REF Number'], row['Exam Type'], row['Exam Name'], row['Mean'], row['Standard Deviation'],
                      row['Highest Achievable Score'], row['Lowest Passing Score/Pass Point'],
                      row['Weight of Exam']))
print(job_code_title_data)
print(exam_data)
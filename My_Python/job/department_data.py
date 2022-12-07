from job_sample_insert import reader
department_data = []
for row in reader:
    department_data.append((row['Department Code'],row['Department Name']))
print(department_data)
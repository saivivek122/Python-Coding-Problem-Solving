from job_sample_insert import *

for row in reader:
    ref_data.append((row['REF Number'], row['Hiring Process'], row['Department Code'],
                     row['Job Code and Title'], row['Certification Rule'], row['Eligible List Specialty'],
                     row['Open Date'], row['Deadline']))
print(ref_data)

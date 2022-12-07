from job_sample_insert import *

eligible_list_data = []
i = 1
for row in reader:
    eligible_list_data.append((i, row['Eligible List Code'], row['Deactivation Date'],
                               row['Original Eligible List Expiration Date'],
                               row['Current Eligible List Expiration Date'],
                               row['Current Eligible List Expiration Date'],
                               row['Inspection Start Date'], row['Inspection End Date'],
                               row['Intended Eligible List Duration (months)']))
    i += 1
print(eligible_list_data)


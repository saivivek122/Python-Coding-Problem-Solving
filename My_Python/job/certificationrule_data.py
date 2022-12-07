from job_sample_insert import *

certificationrule_data = []

reader = take_data(all_data())


def return_certificationrule_data(reader):
    i = 1
    for row in reader:
        certificationrule_data.append((i, row['Certification Rule']))
        i += 1
    print(certificationrule_data)
    return certificationrule_data


return_certificationrule_data(reader)

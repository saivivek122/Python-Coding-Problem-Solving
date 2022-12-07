import csv

with open('C:\\Users\\sdasyapu\\Desktop\\raw_data4.csv', 'r') as f:
    reader = csv.reader(f)
    reader = list(reader)
    data = []
with open('C:\\Users\\sdasyapu\\Desktop\\txt_fro_csv.txt', 'w') as t:
    for row in reader:
        t.write("%s,   %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s \n "%(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]))


    # for row in reader:
    #     if row['Exam_A'] == 'continuous':
    #         data.append((int(row['candidate_id']), row['Exam_A'], int(row['Exam_B']), int(row['Exam_C']),1))
    #     else:
    #         data.append((int(row['candidate_id']), int(row['Exam_A']), int(row['Exam_B']), int(row['Exam_C']),2))
    #
print(reader)

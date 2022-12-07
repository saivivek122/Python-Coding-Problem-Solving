import csv

with open('C:\\Users\\sdasyapu\\Desktop\\raw_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    reader = list(reader)
    print(reader)
    print(len(reader))
    for row in reader:
        a = row[5]
    print(type(a))


def insert_db(csv_reader):
    k = []
    p = []
    candidate_id_index = 0
    primary_key = 13
    while candidate_id_index < len(csv_reader):
        candidate_marks_index = 1
        while candidate_marks_index <= 3:
            candidate_id = csv_reader[candidate_id_index][0]
            ref_id = csv_reader[candidate_id_index][4]
            eligible_list_id = csv_reader[candidate_id_index][5]
            candidate_marks = csv_reader[candidate_id_index][candidate_marks_index]
            data_of_candidate = [ref_id, eligible_list_id, candidate_marks, 1, candidate_marks_index,
                                 candidate_id]
            data_of_candidate.insert(0, primary_key)
            print(data_of_candidate)
            k.append(data_of_candidate)
            p.append(data_of_candidate)
            candidate_marks_index = candidate_marks_index + 1
            primary_key = primary_key + 1
        candidate_id_index = candidate_id_index + 1
    print(p)


insert_db(reader)

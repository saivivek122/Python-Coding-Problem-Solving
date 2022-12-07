import csv
import json
import  boto3
with open('C:\\Users\\sdasyapu\\Desktop\\raw_data.csv', 'r') as f:
    invokeLam = boto3.client("lambda", region_name="us-east-2")
    reader = csv.reader(f)
    next(reader)
    reader = list(reader)
    print(reader[0][5])
    print(len(reader))
    a = []
    for i in range(0,len(reader)):
        a.append(reader[i][5])
    print(a)
    a = list(set(a))
    payload = {"Eligible_lists_to_calculate": json.loads(str(a))}
    resp = invokeLam.invoke(FunctionName="second-function", InvocationType="Event", Payload=json.dumps(payload))

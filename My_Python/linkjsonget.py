import requests
import json
import psycopg2
# print("hello")

# payload = {"postDate": "12/04/2022",
#            "eligibleListId": "2001"}
# response = requests.post("https://6og8i7pe7d.execute-api.us-gov-east-1.amazonaws.com/post-date-post/post-date-post",
#                          data=payload)
# print(response.text)
# data = response.json()
# data = print(json.loads(data["body"]))
# i = input("enter list ")
k = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(k)
# print(response.text)
data = response.json()
print(data['userId'])
# data = json.loads(data["body"])
# print(type(data))
# url = "https://6og8i7pe7d.execute-api.us-gov-east-1.amazonaws.com/post-date-post/post-date-post"
# data = {
#     "postDate" : "12/04/2022",
#     "eligibleListId" : "2001"
# }
# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# r = requests.post(url, data=json.dumps(data), headers=headers)
# # print(r.text)
# a = 20
# b = 40
# c = 30
# if (a>10 and c>10):
#     print("ok")
# print("failed")
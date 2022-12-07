import requests
import json
i_start_data = input("enter start date")
i_end_data = input("enter end date")
end_point = "https://9b851tw8lh.execute-api.us-gov-east-1.amazonaws.com/end-date-post/end-date-post"
data1 = {
	"inspection_end_date": "12/28/2022",
	"inspection_start_date": "12/28/2021",
	"eligible_list_id": "2002"
}
r = requests.post(end_point,data = json.dumps(data1)) #sending json data
print(r.json())

url2 = "https://6i5t6j5fhh.execute-api.us-gov-east-1.amazonaws.com/send-jobs-with-list-id/2001"
response = (requests.get(url2)).json() # getting response data as a json
print(type(response)) # it will be dicty format
# different types of parsing data
print(response['Job_details'])
for i in response['Job_details']:
    print(i["id"])
k = response['Job_details']
print(k)


import requests
import json

url = 'https://httpbin.org/post' 
data = {'ID': '20201690', 'Name' : 'YunSeop Han', 'Department' : 'IoT'}
rsp = requests.post(url, json=data)
print(rsp.text)

response_dict = rsp.json()

print(response_dict['json'])
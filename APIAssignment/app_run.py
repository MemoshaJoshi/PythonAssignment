import json
import requests

def json_run(json_object):
    text = json.dumps(json_object, sort_keys=True, indent=4)
    print(text)

# 1. Create an API that returns title, body of post based on post id.

parameters={'id': 1}
response=requests.get('http://127.0.0.1:5000/posts', params=parameters)
print(response.url)
json_run(response.json())

# 2.Create an API that increase reactions by 10 and displays updated results of provided post id.

parameters={'id': 5}
response=requests.put('http://127.0.0.1:5000/reaction', params=parameters)
print(response.url)
json_run(response.json())

# 3.Create an API that insert new post record and display response message along with updated data.

parameters = {'id': 31, 'title': 'This is a new title', 'body': 'This is a new body', 'user_id': 888, 'tags':['This', 'new','reaction'], 'reactions':'999'}
response=requests.post('http://127.0.0.1:5000/insert', params=parameters)
print(response.url)
print(response.status_code)
json_run(response.json())

# 4. Create an APi that delete posts and display response message based on provided post id.

parameters={'id': 23}
response=requests.delete('http://127.0.0.1:5000/delete', params=parameters)
print(response.url)
json_run(response.json())

# 5. Create an API to return post id, title, body and status in json format that have ‘history’ as tag.
parameters={'history': 'tags'}
response=requests.get('http://127.0.0.1:5000/history', params=parameters)
print(response.url)
json_run(response.json())

# 6. Find any external API besides that given in the assignment. Retrieve the data from that api with the GET operation,,
# clean the data and load it in your local as "example.json" file. Finally, perform all crud operations in that data.
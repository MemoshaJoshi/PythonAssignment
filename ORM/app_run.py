import json
import requests

def json_run(json_object):
    text = json.dumps(json_object, sort_keys=True, indent=4)
    print(text)

parameters={'name': 'cris', 'gender': 'M', 'age': 36, 'phone': 981787878}
response=requests.post('http://127.0.0.3:5000/add_customer', params=parameters)
print(response.url)
json_run(response.json())

parameters={'check_in' : '2018-01-08', 'check_out' : '2018-01-10' , 'room_type': 'deluxe'}
response=requests.get('http://127.0.0.3:5000/price_stay', params=parameters)
print(response.url)
json_run(response.json())

parameters={'check_in' : '2018-01-08', 'check_out' : '2018-01-10' , 'room_id': 1, 'payment' : 'yes', 'customer_id': 1}
response=requests.post('http://127.0.0.3:5000/add_booking', params=parameters)
print(response.url)
json_run(response.json())

parameters={'check_in' : '2019-01-10', 'check_out' : '2019-01-12' , 'room_id': 1}
response=requests.get('http://127.0.0.3:5000/track_status', params=parameters)
print(response.url)
json_run(response.json())




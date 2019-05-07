import requests

url_base = 'http://127.0.0.1:5000/api/chainsaw'

dave_data = {'name':'Dave', 'catches':12, 'country':'USA'}
response = requests.post(url_base, data=dave_data)
if response.status_code == requests.codes.created:
    print('Dave Record was created')
else:
    response.raise_for_status()

zoe_data = {'name':'Zoe', 'catches':42, 'country':'Canada'}
response = requests.post(url_base, data=zoe_data)
if response.status_code == requests.codes.created:
    print('Zoe Record was created')
else:
    response.raise_for_status()


    # get all records

response = requests.get(url_base)
print(response.json(), response.status_code)
if response.status_code == requests.codes.ok:
    data = response.json()
    for index, record in enumerate(data):
        print(index, record)
else:
    response.raise_for_status()



import requests

data = requests.get('https://catfact.ninja/fact').json()

print(data)

fact = data['fact']
print(fact)
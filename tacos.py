import requests

random_taco = requests.get('https://taco-randomizer.herokuapp.com/random').json()
print(random_taco)

# print(random_taco['mixin']['recipe'])

for part, recipe in random_taco.items():
    title = part.replace('_',' ').title()
    print(f'\n********{title}********')
    print(f'\n{recipe["recipe"]}')
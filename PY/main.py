import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
token = "1f4bb07ff68025c5df29be75a3b73581"
header = {"Content-Type":"application/json", "trainer_token": token}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_put = {
    "pokemon_id": "171795",
    "name": "New Name",
    "photo_id": 1
}
body_add = {
    "pokemon_id": "171795"
}

response_create = requests.post(url = f"{URL}/pokemons", headers = header, json = body_create)
print(response_create.text)

response_put = requests.put(url = f"{URL}/pokemons", headers = header, json = body_put)
print(response_put.text)

response_addpokeball = requests.post(url = f"{URL}/trainers/add_pokeball", headers = header, json = body_add)
print(response_addpokeball.text)







import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
token = "1f4bb07ff68025c5df29be75a3b73581"
header = {"Content-Type":"application/json", "trainer_token": token}
trainer_id = "16527"

def test_status_code():
    response = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : trainer_id})
    assert response.status_code == 200

def test_status_name():
    response_get = requests.get(url=f"{URL}/trainers", params = {"trainer_id": trainer_id})
    assert response_get.json()["data"][0]["trainer_name"] == "Карпатыч"


import requests
import jsonpath
import json

def test_delete_of_a_user():
    url = "https://reqres.in/api/users/2"
    response = requests.delete(url)
    assert response.status_code == 204

    # parse to the json format
    response = json.loads(response.text)
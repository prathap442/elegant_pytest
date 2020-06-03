import json
import requests
import pdb
import jsonpath

def test_reqres_response():
  url = "https://reqres.in/api/users/2"
  response = requests.get(url)
  # parse to the json format
  json_response = json.loads(response.text)
  json_first_name = jsonpath.jsonpath(json_response,'first_name')
  pdb.set_trace()
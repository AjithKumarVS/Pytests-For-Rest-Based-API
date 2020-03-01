import requests
import json

def test_sentence_storing():
    url='http://localhost:5000/store'
    json_input={"username":"Test01", "password":"Digital Factory", "sentence":"Geo-Fencing"}
    response=requests.post(url,json=json_input)
    assert response.status_code==200

    json_data=response.json()
    assert json_data["msg"]=="Sentence saved successfully"
    assert json_data["status"]==200

def test_tokens():
    url='http://localhost:5000/store'
    json_input={"username":"Test01", "password":"Digital Factory", "sentence":"Geo-Fencing"}
    response=requests.post(url,json=json_input)
    assert response.status_code==200

    json_data=response.json()
    assert json_data["status"]==301

def test_username_pw_match():
    url='http://localhost:5000/store'
    json_input={"username":"Test01", "password":"Digital Factory", "sentence":"Geo-Fencing"}
    response=requests.post(url,json=json_input)
    assert response.status_code==200

    json_data=response.json()
    assert json_data["status"]==302







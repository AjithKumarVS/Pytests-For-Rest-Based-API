import requests
import json

def test_sentence_retrieval():
    url='http://localhost:5000/get'
    json_input={"username":"Test01", "password":"Digital Factory"}
    response=requests.post(url,json=json_input)
    assert response.status_code==200

    json_data=response.json()
    assert json_data["sentence"]=="Geo-Fencing"
    assert json_data["status"]==200

def test_tokens():
    url='http://localhost:5000/get'
    json_input={"username":"Test01", "password":"Digital Factory"}
    response=requests.post(url,json=json_input)
    assert response.status_code==200

    json_data=response.json()
    assert json_data["status"]==301

def test_username_pw_match():
    url='http://localhost:5000/get'
    json_input={"username":"Test01", "password":"Digital Factory"}
    response=requests.post(url,json=json_input)
    assert response.status_code==200

    json_data=response.json()
    assert json_data["status"]==302


  


   


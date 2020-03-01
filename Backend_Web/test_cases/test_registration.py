import requests
import json

def test_registration():
    url='http://localhost:5000/register'
    json_input={"username":"Test01", "password":"Digital Factory"}
    response=requests.post(url,json=json_input)
    assert response.status_code==200

    json_data=response.json()
    assert json_data["msg"]=="You successfully signed up for the API"
    assert json_data["status"]==200




  


   


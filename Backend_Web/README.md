# Python REST API

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to setup your virtual environment. 

(This is a Linux/Mac OS setup guide)

```bash
$  pip install virtualenv
$  pip install pytest
$  source venv/bin/activate
$  pip install -r requirements.txt
```
Install [Postman](https://www.getpostman.com/downloads/)

Install [Docker](https://docs.docker.com/v17.09/engine/installation/)

Install [Docker-compose](https://docs.docker.com/v17.09/engine/installation/)

## Building the API

```bash
$ sudo docker-compose build
$ sudo docker-compose up 
```

## Testing in Postman
REGISTER AN ACCOUNT
- localhost:5000/register
```JSON
{
  "username": "<Enter username here>",
  "password": "<Enter password here>"
}
```
RETURN MESSAGE:
```JSON
{
  "msg": "You successfully signed up for the API",
  "status": "200"
}
```
STORE SENTENCE USING CREDENTIALS CREATED 
- localhost:5000/store
```JSON
{
  "username": "<Enter username here>",
  "password": "<Enter password here>",
  "sentence": "<Enter sentence here>"
}
```
RETURN MESSAGE
```JSON
{
    "msg": "Sentence saved successfully",
    "status": 200
}
```

RETRIEVE YOUR MESSAGE:
- localhost:5000/get
```JSON
{
  "username": "<Enter username here>",
  "password": "<Enter password here>"
}
```
RETURN MESSAGE:
```JSON
{
    "sentence": "<Your stored sentence>",
    "status": 200
}
```
IF YOU ARE OUT OF TOKENS: 
```JSON
{
    "status": 301
}
``` 
## Challenge
The challenge is to create pytest's that create a users account, stores a sentence using the credentials you created, and retrieves the sentence you stored. 

1. Navigate to test_cases
2. In test_registration.py write a function that registers a users account. 
3. In test_sentence_storing.py write a function that stores a sentence to the users account you created.
4. In test_sentence_retrieval.py write a function that retrieves the sentence you stored. 
5. Submit work!

## Helpful links
- https://docs.pytest.org/en/latest/
- https://requests.readthedocs.io/en/master/






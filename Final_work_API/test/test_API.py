import requests


def test_search_k():

    json = {
      "X-API-KEY": "QBZZCZX-DW5M2RB-G0DKZ6R-QE5X8PS"
    }
    response = requests.get("https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10&query=Корона", headers=json)
    
    assert response.status_code == 200

def test_search_id():

    json = {
      "X-API-KEY": "QBZZCZX-DW5M2RB-G0DKZ6R-QE5X8PS"
    }
    response = requests.get(" https://api.kinopoisk.dev/v1.4/movie/924910", headers=json)
    
    assert response.status_code == 200

    assert response.json()["description"] == "История королевы Елизаветы II с момента её свадьбы в 1947 году до настоящего времени."

def test_search_id_aktr():

    json = {
      "X-API-KEY": "QBZZCZX-DW5M2RB-G0DKZ6R-QE5X8PS"
    }
    response = requests.get("https://api.kinopoisk.dev/v1.4/person/54829", headers=json)
    
    assert response.status_code == 200

def test_search_id_picture():

    json = {
      "X-API-KEY": "QBZZCZX-DW5M2RB-G0DKZ6R-QE5X8PS"
    }
    response = requests.get("https://api.kinopoisk.dev/v1.4/image?page=1&limit=1", headers=json)
    
    assert response.status_code == 200



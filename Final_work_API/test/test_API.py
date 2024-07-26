import requests
import allure

@allure.title("Поиск фильма по названию на кириллице") 
@allure.description("Тест проверяет поиск фильма по названию на кириллице") 
@allure.feature("READ") 
@allure.severity("критичский")
def test_search_k():
    with allure.step("Создание хедеров"):
        json = {
      "X-API-KEY": "QBZZCZX-DW5M2RB-G0DKZ6R-QE5X8PS"
    }
    with allure.step("отправка запроса"):   
        response = requests.get("https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10&query=Корона", headers=json)
    with allure.step("проверка результата"):    
        assert response.status_code == 200

@allure.title("Поиск фильма по id") 
@allure.description("Тест проверяет поиск фильма по id") 
@allure.feature("READ") 
@allure.severity("критичский")
def test_search_id():
    with allure.step("Создание хедеров"):
        json = {
      "X-API-KEY": "QBZZCZX-DW5M2RB-G0DKZ6R-QE5X8PS"
    }
    response = requests.get(" https://api.kinopoisk.dev/v1.4/movie/924910", headers=json)
    
    assert response.status_code == 200

    assert response.json()["description"] == "История королевы Елизаветы II с момента её свадьбы в 1947 году до настоящего времени."

@allure.title("Поиск фильма по id актера") 
@allure.description("Тест проверяет поиск фильма по id актера") 
@allure.feature("READ") 
@allure.severity("критичский")
def test_search_id_aktr():

    json = {
      "X-API-KEY": "QBZZCZX-DW5M2RB-G0DKZ6R-QE5X8PS"
    }
    response = requests.get("https://api.kinopoisk.dev/v1.4/person/54829", headers=json)
    
    assert response.status_code == 200

@allure.title("Поиск картинки") 
@allure.description("Тест проверяет поиск картинки") 
@allure.feature("READ") 
@allure.severity("критичский")
def test_search_id_picture():

    json = {
      "X-API-KEY": "QBZZCZX-DW5M2RB-G0DKZ6R-QE5X8PS"
    }
    response = requests.get("https://api.kinopoisk.dev/v1.4/image?page=1&limit=1", headers=json)
    
    assert response.status_code == 200



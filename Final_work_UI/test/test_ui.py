from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture 
def driver(): 
    browser = webdriver.Chrome() 
    browser.maximize_window() 
    browser.implicitly_wait(4)
    yield browser 
    browser.quit()

def test_search(driver):
    driver.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")
    sleep(1)
    driver.find_element(By.NAME,"kp_query").send_keys("Троя")
    driver.find_element(By.ID,"suggest-item-film-3442").click()
    sleep(1)
    assert driver.find_element(By.CSS_SELECTOR,"span[data-tid='75209b22']").text == "Троя (2004)"

def test_search_2(driver):
    driver.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")
    sleep(1)
    driver.find_element(By.NAME,"kp_query").send_keys("Troy")
    driver.find_element(By.ID,"suggest-item-film-3442").click()
    sleep(1)
    assert driver.find_element(By.CSS_SELECTOR,"span[data-tid='75209b22']").text == "Троя (2004)"

def test_bilet(driver):
    driver.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")
    driver.implicitly_wait(10)
    #driver.find_element(By.CSS_SELECTOR,"a[data-tid='de7c6530']")
    driver.find_element(By.NAME,"kp_query").send_keys("Троя")
    driver.find_element(By.ID,"suggest-item-film-3442").click()
    driver.find_element(By.CSS_SELECTOR,'[title="Буду смотреть"]').click()
    assert driver.find_element(By.CSS_SELECTOR,'.AuthLoginInputToggle-input')





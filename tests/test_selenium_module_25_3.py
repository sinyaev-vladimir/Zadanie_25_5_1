
# Другой способ вызова хром драйвера в отличии от файла test_selenium_petfriends

import time
from conftest import *



# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_show_my_pets():

   # Ожидаем что на странице появится поле с id=email
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "email")))

   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('qwerty3@mail')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('qwerty3')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя

   # Ожидаем что в теге title появится искомая фраза
   element = WebDriverWait(pytest.driver, 10).until(
      EC.title_is("PetFriends: My Pets"))


   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   pytest.driver.find_element_by_xpath('//body / nav[1] / button[1] / span[1]').click()

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "navbarNav")))


   pytest.driver.find_element_by_xpath('//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "all_my_pets")))


   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
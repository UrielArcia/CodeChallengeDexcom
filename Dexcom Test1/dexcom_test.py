import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#traer archivo, path with the file location
credentials = r'C:\Users\afore.jarcia\Documents\dexcom\Dexcom Test1\credentials.xlsx'

#leer archivo, read file with credentials
rc = pandas.read_excel(credentials)

user = rc['username'][0]
psw = rc['password'][0]

url = 'https://clarity.dexcom.com/'

#selectores selectors
selector_btn_home_users = 'body > div.wrapper > div.torso.torso-content-container > div > div.main-landing > div > nav > ul > li.panel.home-user > div > a'
selector_username = '#username'
selector_password = '#password'
selector_btn_login = '#edit-actions > input'

# Abrir el navegador/ open Browser
driver = webdriver.Chrome()
#maximizar la pantalla
driver.maximize_window()
driver.get(url)

#Actions to do:
#press login button
#driver.find_element_by_css_selector(selector_btn_login).click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, selector_btn_home_users).click()
#loggin usr/psw
time.sleep(3)
#driver.find_element_by_css_selector(selector_username).send_keys(user)
driver.find_element(By.CSS_SELECTOR, selector_username).send_keys(user)
time.sleep(1)
#driver.find_element_by_css_selector(selector_password).send_keys(psw)
driver.find_element(By.CSS_SELECTOR, selector_password).send_keys(psw)
#press btn login
#driver.find_element_by_css_selector(selector_btn_login).click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, selector_btn_login).click()
time.sleep(5)
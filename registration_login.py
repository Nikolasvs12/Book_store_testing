#Registration_login: регистрация аккаунта

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)

my_m = driver.find_element_by_link_text("My Account").click()
time.sleep(2)

reg_m = driver.find_element_by_id("reg_email")
reg_m.send_keys("kdelu@rambler.ru")

reg_p = driver.find_element_by_id("reg_password")
reg_p.send_keys("223344Bs!@#")

reg_btn = driver.find_element_by_name("register").click()

driver.close()

#Registration_login 2

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)

my_m = driver.find_element_by_link_text("My Account").click()
time.sleep(2)

us_m = driver.find_element_by_id("username")
us_m.send_keys("kdelu@rambler.ru")

us_p = driver.find_element_by_id("password")
us_p.send_keys("223344Bs!@#")

log_btn = driver.find_element_by_name("login").click()

text_check = WebDriverWait(driver, 10 ).until(
EC.text_to_be_present_in_element((By.LINK_TEXT, "Logout"), "Logout"))

driver.quit()






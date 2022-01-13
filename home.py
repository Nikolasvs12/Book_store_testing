import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)

n_cl = driver.find_element_by_css_selector(".post-160 h3").click()
time.sleep(1)

rev_cl = driver.find_element_by_class_name("reviews_tab").click()
time.sleep(1)

f_st = driver.find_element_by_class_name("star-5").click()
time.sleep(1)

com = driver.find_element_by_id("comment")
com.send_keys("Nice book!")

aut_com = driver.find_element_by_id("author")
aut_com.send_keys("Mike")

m_com = driver.find_element_by_id("email")
m_com.send_keys("123@yandex.ru")
time.sleep(1)

sub_btn = driver.find_element_by_id("submit")
time.sleep(1)

driver.quit()






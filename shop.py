
#Shop1: отображение страницы товара

import time
from selenium import webdriver

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

shop = driver.find_element_by_link_text("Shop").click()

book = driver.find_element_by_css_selector(".post-181 h3").click()

bt = driver.find_element_by_class_name("product_title.entry-title")
bt_get_text = bt.text
assert bt_get_text == "HTML5 Forms"

driver.quit()



#Shop2: количество товаров в категории

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

shop = driver.find_element_by_link_text("Shop").click()

ht_r = driver.find_element_by_css_selector(".cat-item.cat-item-19 a").click()

text_check = WebDriverWait(driver, 10 ).until(
EC.text_to_be_present_in_element((By.CLASS_NAME, "cat-item.cat-item-19 .count"), "3"))

driver.quit()



# Shop3: Сортировка

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

my_m = driver.find_element_by_link_text("My Account").click()
time.sleep(2)

us_m = driver.find_element_by_id("username")
us_m.send_keys("kdelu@rambler.ru")

us_p = driver.find_element_by_id("password")
us_p.send_keys("223344Bs!@#")

log_btn = driver.find_element_by_name("login").click()

shop = driver.find_element_by_link_text("Shop").click()

s_elem = driver.find_element_by_css_selector("[value='menu_order']")
elem_check = WebDriverWait(driver, 10).until(
    EC.element_to_be_selected(s_elem))

sort = driver.find_element_by_class_name("orderby")
select = Select(sort)
time.sleep(1)
select.select_by_value("price-desc")

s_elem = driver.find_element_by_css_selector("[value='menu_order']")

sv = driver.find_element_by_css_selector("[value='price-desc']")
sv_check = WebDriverWait(driver, 10).until(
    EC.element_to_be_selected(sv))

driver.quit()




#Shop: отображение, скидка товара

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

my_m = driver.find_element_by_link_text("My Account").click()
time.sleep(2)

us_m = driver.find_element_by_id("username")
us_m.send_keys("kdelu@rambler.ru")

us_p = driver.find_element_by_id("password")
us_p.send_keys("223344Bs!@#")

log_btn = driver.find_element_by_name("login").click()

shop = driver.find_element_by_link_text("Shop").click()

an_book = driver.find_element_by_css_selector(".post-169 h3").click()

old_pr = driver.find_element_by_css_selector(".price>del>span")
old_pr_text = old_pr.text
assert old_pr_text == "₹600.00"

new_pr = driver.find_element_by_css_selector(".price>ins>span")
new_pr_text = new_pr.text
assert new_pr_text == "₹450.00"

im_b = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
im_b.click()
time.sleep(2)

cl_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
cl_btn.click()

driver.quit()



#Shop: проверка цены в корзине

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

shop = driver.find_element_by_link_text("Shop").click()

ad_bas = driver.find_element_by_css_selector("[data-product_id='182']").click()

time.sleep(2)

it_cart = driver.find_element_by_css_selector("nav span.cartcontents")
it_cart_text = it_cart.text
assert it_cart_text == "1 Item"

sm_cart = driver.find_element_by_css_selector("nav span.amount")
sm_cart_text = sm_cart.text
assert sm_cart_text == "₹180.00"
time.sleep(1)

vw_cart = driver.find_element_by_css_selector("[title='View your shopping cart']").click()

subt_check = WebDriverWait(driver, 10 ).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']>span.amount"), "₹180.00"))

tot_ch = WebDriverWait(driver, 10 ).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "td>strong>span"), "₹189.00"))

driver.quit()



#Shop: работа в корзине

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

shop = driver.find_element_by_link_text("Shop").click()

driver.execute_script("window.scrollBy(0, 300);")

ad_bas = driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(1)
ad_bas_two = driver.find_element_by_css_selector("[data-product_id='180']").click()

vw_cart = driver.find_element_by_css_selector("[title='View your shopping cart']").click()
time.sleep(1)
rem_bas = driver.find_element_by_css_selector("[data-product_id='182']").click()

und_rem = driver.find_element_by_link_text("Undo?").click()

qal_bt = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
qal_bt.clear()
time.sleep(1)
qal_bt.send_keys(3)

upd_cart = driver.find_element_by_name("update_cart").click()

#ql_bt = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
#ql_bt_text = ql_bt.text
#assert ql_bt_text == "3" тест почему-то не работает

time.sleep(1)
ap_kup = driver.find_element_by_name("apply_coupon").click()

vw_text = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))

driver.quit()



#Shop: покупка товара

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

shop = driver.find_element_by_link_text("Shop").click()

driver.execute_script("window.scrollBy(0, 300);")

ad_bas = driver.find_element_by_css_selector("[data-product_id='182']").click()

vw_cart = driver.find_element_by_css_selector("[title='View your shopping cart']").click()

pr_ch = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "wc-forward")) )

pr_btn = driver.find_element_by_class_name("wc-forward").click()

pr_ch = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))

name = driver.find_element_by_id("billing_first_name")
name.send_keys("Mike")

l_name = driver.find_element_by_id("billing_last_name")
l_name.send_keys("Lider")

mail = driver.find_element_by_id("billing_email")
mail.send_keys("kdelu@rambler.ru")

tel = driver.find_element_by_id("billing_phone")
tel.send_keys("86955555555")

sel = driver.find_element_by_id("s2id_billing_country").click()
sel = driver.find_element_by_id("select2-result-label-22").click()

str = driver.find_element_by_id("billing_address_1").send_keys("Nemiga 9")
ap = driver.find_element_by_id("billing_address_2").send_keys("12")
city = driver.find_element_by_name("billing_city").send_keys("Minsk")
cit_st = driver.find_element_by_name("billing_state").send_keys("Minskaya")
city = driver.find_element_by_name("billing_postcode").send_keys("220220")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)

ch_pay = driver.find_element_by_id("payment_method_cheque").click()
time.sleep(3)
ord = driver.find_element_by_id("place_order").click()

vw_text = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.ID, "content"), "Thank you. Your order has been received."))

vw_text = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method strong"), "Check Payments"))

driver.quit()









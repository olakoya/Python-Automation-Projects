import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys

URL = "https://www.crawco.co.uk/"

driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver.get(URL)

fb_btn = driver.find_element_by_class_name("fa-facebook-f")
fb_btn.click()

driver.implicitly_wait(30)

# confirm_not_now = driver.find_element_by_id("expanding_cta_close_button")
# confirm_not_now.click()

# driver.implicitly_wait(10)

# fb_login = driver.find_element_by_class_name("_4jy1")
# fb_login.click()

# driver.implicitly_wait(10)

def login(username):
    user = driver.find_element_by_css_selector("#email")
    user.clear()
    user.send_keys(username)

def passwd(password):
    passw = driver.find_element_by_css_selector("#pass")
    passw.clear()
    passw.send_keys(password)

driver.implicitly_wait(10)
login("b****d@gmail.com")
passwd("*******")

driver.implicitly_wait(10)

submit = driver.find_element_by_name("login")
submit.click()
time.sleep(5)
driver.close()

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

# add the paths to your downloaded chromedriver. 
# chromedriver version must match google chrome version
driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver.get('https://ember-static-staging.fatsoma.com/e/oyy0k8pt/test')

time.sleep(10)

login = driver.find_element_by_id("ember411")

time.sleep(5)
login.send_keys(Keys.RETURN)

time.sleep(15)

def login(username):
    user = driver.find_element_by_name("email")
    user.clear()
    user.send_keys(username)

def passwd(password):
    passw = driver.find_element_by_name("current-password")
    passw.clear()
    passw.send_keys(password)

# add your login details
login()
passwd()

time.sleep(5)

submit = driver.find_element_by_css_selector("body > div:nth-child(3) > div > div._container_1w4bwn._container_86f63p > div > div:nth-child(2) > form > div.Mt-40.Mb-10._btn_1lqrws > button")
submit.click()

time.sleep(5)

ticket_number = driver.find_element_by_css_selector("tr._row_1i6qvv:nth-child(1) > td:nth-child(3) > div:nth-child(1) > div:nth-child(1) > select:nth-child(2)")
ticket_number.send_keys("1")
# ticket_number.send_keys(Keys.RETURN)

time.sleep(5)

submit_ticket = driver.find_element_by_css_selector("._button_6qxt1u > button:nth-child(1)")
submit_ticket.click()

time.sleep(15)

confirm_ticket = driver.find_element_by_css_selector("._button_192h79")
confirm_ticket.click()

time.sleep(5)

confirm_email = driver.find_element_by_css_selector("#ember725")
# add your email to confirm
confirm_email.send_keys("123456@gmail.com")

time.sleep(5)

confirm_btn = driver.find_element_by_css_selector("._button_192h79")
confirm_btn.click()

# confirm = driver.find_elements_by_css_selector("body > div > div > div._container_1w4bwn._container_i0ckhx > div > article > div > form > div._button_1t4ys8 > button")
# confirm.click()

time.sleep(25)

driver.close()

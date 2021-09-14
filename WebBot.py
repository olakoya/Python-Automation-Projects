from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


# driver = webdriver.Chrome('Projects\walmart bot\chromedriver.exe')

driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver.get('https://www.walmart.com/')

driver.implicitly_wait(10)

search_bar = driver.find_element_by_name("query")
shoe = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/section/section/div[2]/div/div[3]/div[2]/div/form/input[2]")
shoe.clear()
shoe.send_keys("Books")
time.sleep(5)
search_bar.clear()
search_bar.send_keys("laptops")
time.sleep(5)
search_bar.send_keys(Keys.RETURN)

try:
    element = driver.find_element_by_xpath('//*[@id="vScpPdzESmlmJGz"]')
    action = ActionChains(driver)
    action.click_and_hold(element).perform()
    # action.perform()
except:
    print("no element found")

product = driver.find_element_by_link_text('HP 15.6" FHD, Celeron N4020, 4GB RAM, 128GB SSD, Black, Windows 10 Home in S mode plus Microsoft Office, 15-dw1001wm')

product.send_keys(Keys.RETURN)
time.sleep(10)

add_to_cart = driver.find_element_by_xpath('//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button')
add_to_cart.send_keys(Keys.RETURN)
driver.implicitly_wait(25)

# driver.close()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'), "$100"))
price = browser.find_element_by_xpath('//button[@id="book"]')
price.click()

xnumber = browser.find_element_by_xpath('//span[@id="input_value"]')
x = xnumber.text
print(x)










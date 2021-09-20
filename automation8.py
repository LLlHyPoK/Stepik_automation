from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Firefox()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price" ), '100' ))
button = browser.find_element_by_xpath('//*[@id="book"]').click()

x_number = browser.find_element_by_xpath('//*[@id="input_value"]')
x = x_number.text
x = float(x)
y = math.log(abs(12*math.sin(x)))
y = str(y)
input = browser.find_element_by_xpath('//*[@id="answer"]')
input.send_keys(y)

submit = browser.find_element_by_xpath('/html/body/form/div/div/button').click()


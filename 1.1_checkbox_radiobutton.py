from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()

    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()

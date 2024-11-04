from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:

    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, "input_value").text
    y = calc(x_element)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    time.sleep(1)

    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robotCheckbox.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

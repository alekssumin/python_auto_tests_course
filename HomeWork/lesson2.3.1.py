import math

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

try:

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CLASS_NAME, "btn-primary")
    btn.click()

    alert = browser.switch_to.alert
    alert.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    # time.sleep(1)

    # robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    # robotCheckbox.click()
    #
    # robotsRule = browser.find_element(By.ID, "robotsRule")
    # robotsRule.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

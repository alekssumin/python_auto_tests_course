import math

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

try:

    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

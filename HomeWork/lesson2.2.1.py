from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:

    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    sumNum = str((int(num1) + int(num2)))


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sumNum)

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()

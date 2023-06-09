import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/python/python_classes.asp")
driver.maximize_window()
driver.delete_all_cookies()

time.sleep(5)
# forLoopsElement = driver.find_element(By.LINK_TEXT, "Python For Loops")
forLoopsElement = driver.find_element(By.PARTIAL_LINK_TEXT, "For Loops")
forLoopsElement.click()
time.sleep(5)

driver.close()

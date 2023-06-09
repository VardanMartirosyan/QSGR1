import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()


searchFieldElement = driver.find_element(By.ID, 'APjFqb')
searchFieldElement.send_keys("Ferrari Enzo")
time.sleep(1)
searchFieldElement.send_keys(Keys.ENTER)
time.sleep(5)

driver.close()
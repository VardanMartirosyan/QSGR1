from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.youtube.com")
searchFieldElement = driver.find_element(By.NAME, "search_query")
searchFieldElement.clear()
searchFieldElement.send_keys("Selenium tutorial")
time.sleep(3)

searchButtonElement = driver.find_element(By.ID, "search-icon-legacy")
searchButtonElement.click()
time.sleep(5)

driver.close()
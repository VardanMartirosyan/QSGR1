import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.youtube.com")
driver.maximize_window()
driver.delete_all_cookies()

searchFieldElement = driver.find_element(By.NAME, "search_query")
searchFieldElement.clear()
searchFieldElement.send_keys("stylish")
searchFieldElement.send_keys(Keys.ENTER)

searchButtonElement = driver.find_element(By.ID, "search-icon-legacy")
searchButtonElement.click()
time.sleep(3)

# firstVidoElement = driver.find_element(By.XPATH, "(//div[@id='title-wrapper'])[1]")
# firstVidoElement = driver.find_element(By.ID, "title-wrapper")
firstVidoElement = driver.find_elements(By.ID, "title-wrapper")
firstVidoElement[0].clicck()
time.sleep(3)


driver.close()

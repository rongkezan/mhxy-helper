from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com")
print(driver.title)
search_box = driver.find_element(By.NAME, "q")
print(search_box)
search_button = driver.find_element(By.NAME, "btnK")
print(search_button)
from selenium import webdriver
from selenium.webdriver.common.by import By
LINK = "https://orteil.dashnet.org/experiments/cookie/"

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)
driver = webdriver.Chrome()
driver.get(LINK)
attack = driver.find_element(By.ID, value="cookie")
while True:
    attack.click()

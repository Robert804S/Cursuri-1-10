from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# initializam chrome

chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.maximize_window()

chrome.get("https://formy-project.herokuapp.com/form")

first_name = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.ID, "first-name")))
first_name.send_keys("Robert")
sleep(2)

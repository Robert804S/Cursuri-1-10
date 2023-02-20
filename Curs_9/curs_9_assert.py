from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# initializam chrome

chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.maximize_window()

chrome.get("https://formy-project.herokuapp.com")

chrome.find_element(By.LINK_TEXT, "Autocomplete").click()
expected_url = "https://formy-project.herokuapp.com/autocomplete"
actual = chrome.current_url

assert actual == expected_url, "invalid url"

chrome.quit()
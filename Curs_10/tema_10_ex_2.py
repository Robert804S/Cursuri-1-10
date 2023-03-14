"""
Scrieti cel putin 3 functii de test intr-o clasa (cum am facut la clasa)
Folositi firefox in loc de chrome
"""

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# pentru a rula teste pe Firefox, cu versiunea selenium 4.6.0
# driver = webdriver.Firefox()

class Exercitiul_2(unittest.TestCase):

    CONTEXT_MENU = (By.LINK_TEXT, "Context Menu")
    PATRAT = (By.ID, "hot-spot")
    JAVA_SCRIPT_ALERTS = (By.XPATH, "//a[normalize-space()='JavaScript Alerts']")
    CLICK_FOR_JS_PROMPT = (By.XPATH, "//button[@onclick='jsPrompt()']")
    RESULT_MESSAGE = (By.ID, 'result')
    FORM_AUTHENTICATION = (By.XPATH, "//a[normalize-space()='Form Authentication']")
    USERNAME = (By.ID, "username")

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/")
        sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_1(self):   # Click dreapta
        self.driver.find_element(*self.CONTEXT_MENU).click() # accesam pagina context menu
        sleep(2)
        cutia_patata = self.driver.find_element(*self.PATRAT)
        action = ActionChains(self.driver)
        action.context_click(cutia_patata).perform()
        # ActionChains(self.driver).context_click(self.driver.find_element(*self.PATRAT)).perform()
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(2)

    def test_2(self):   # Prompt message
        self.driver.find_element(*self.JAVA_SCRIPT_ALERTS).click() # accesam pagina Java Script Alerts
        sleep(2)
        self.driver.find_element(*self.CLICK_FOR_JS_PROMPT).click()
        sleep(2)
        new_small_window = self.driver.switch_to.alert
        print(f"Textul aparut este {new_small_window.text}")

        textul_meu = "Buna seara!"
        new_small_window.send_keys(textul_meu)
        sleep(2)
        new_small_window.accept()
        sleep(2)
        result_text = self.driver.find_element(*self.RESULT_MESSAGE).text
        assert result_text == f"You entered: {textul_meu}"
        print("Totul este OK!")

    def test_3(self):   # Login Page (tomsmith + SuperSecretPassword!)
        self.driver.find_element(*self.FORM_AUTHENTICATION).click()
        field = self.driver.find_element(*self.USERNAME)
        sleep(2)
        field.send_keys("tomsmith")
        sleep(2)
        field.send_keys(Keys.TAB + "SuperSecretPassword!" + Keys.TAB + Keys.ENTER)
        sleep(5)




from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# https://selectorshub.com/selectorshub/

'''
Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri

- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
Interactionează cu un element la alegere din listă.
'''

class Selectors():
    chrome = webdriver.Chrome(ChromeDriverManager().install())

    def __init__(self):
        # self.chrome.get("https://formy-project.herokuapp.com/autocomplete")
        self.chrome.maximize_window()

    INPUT_ADDRESS = (By.ID, 'autocomplete')

    def address_field(self):
        self.chrome.get("https://formy-project.herokuapp.com/autocomplete")
        sleep(3)
        address_text_field = self.chrome.find_element(*self.INPUT_ADDRESS).send_keys('Jud. Sibiu')
        # adress_text_field.send_keys('Jud. Sibiu')


    AUTOCOMPLETE = (By.LINK_TEXT, 'Autocomplete')

    def click_autocomplete(self):
        self.chrome.get("https://formy-project.herokuapp.com/")
        sleep(3)
        click_on_autocomplete = self.chrome.find_element(*self.AUTOCOMPLETE)
        click_on_autocomplete.click()


    DRAG_AND_DROP = (By.PARTIAL_LINK_TEXT, 'Drag and')

    def click_drag_and_drop(self):
        self.chrome.get('https://formy-project.herokuapp.com')
        sleep(3)
        self.chrome.find_element(*self.DRAG_AND_DROP).click()


    INPUT_FIRSTNAME = (By.NAME, 'firstname')
    def complete_name(self):
        self.chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
        sleep(3)
        click_accept_all = self.chrome.find_element(By.ID, "ez-accept-all").click()
        sleep(3)
        complete_name_field = self.chrome.find_element(*self.INPUT_FIRSTNAME).send_keys('Robert')


    KEY_PRESSES = (By.TAG_NAME, 'input')

    def input_key(self):
        self.chrome.get('https://the-internet.herokuapp.com/key_presses?')
        sleep(3)
        self.chrome.find_element(*self.KEY_PRESSES).send_keys('Robert')


    COUNTRY = (By.CLASS_NAME, 'form-control')

    def write_your_country(self):
        self.chrome.get('https://formy-project.herokuapp.com/autocomplete')
        sleep(3)
        input_your_address = self.chrome.find_elements(*self.COUNTRY)
        input_your_address[6].send_keys('Romania')


    INPUT_ADDRESS_2 = (By.CSS_SELECTOR, '#autocomplete')

    def write_address(self):
        self.chrome.get('https://formy-project.herokuapp.com/autocomplete')
        sleep(3)
        self.chrome.find_element(*self.INPUT_ADDRESS).send_keys('Judetul Sibiu')


    INPUT_CITY = (By.XPATH, "//input[@id='locality']")

    def write_your_city(self):
        self.chrome.get('https://formy-project.herokuapp.com/autocomplete')
        sleep(3)
        self.chrome.find_element(*self.INPUT_CITY).send_keys('Sibiu')


activitate_1 = Selectors()
# activitate_1.address_field()
# sleep(3)

# activitate_1.click_autocomplete()
# sleep(3)

# activitate_1.click_drag_and_drop()
# sleep(3)

# activitate_1.complete_name()
# sleep(3)

# activitate_1.input_key()
# sleep(3)

# activitate_1.write_your_country()
# sleep(3)

# activitate_1.write_address()
# sleep(3)

activitate_1.write_your_city()
sleep(3)

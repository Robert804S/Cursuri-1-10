from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# https://formy-project.herokuapp.com/form

class Selectors():
    chrome = webdriver.Chrome(ChromeDriverManager().install())

#  cream constante in functie de selectorii pe care ii folosim

    INPUT_FIRST_NAME = (By.ID, 'first-name')
    INPUT_LAST_NAME = (By.CLASS_NAME, 'form-control')
    RADIO_BUTTON = (By.CSS_SELECTOR, 'input#radio-button-1')
    AUTOCOMPLETE_LINK_TEXT = (By.LINK_TEXT, 'Autocomplete')
    ENABLE_DISABLED_LINK = (By.PARTIAL_LINK_TEXT, 'Enabled')
    INPUT_FIRST_NAME_BY_XPATH = (By.XPATH, '//input@class="form-control"')

    def __init__(self):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        self.chrome.maximize_window()

    def first_name_field(self, first_name):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        first_name_text_field = self.chrome.find_element(*self.INPUT_FIRST_NAME)  # first_name_text_field va fi elementul de pe pagina cu id-ul first_name
        first_name_text_field.send_keys(first_name)

    def last_name_field(self, last_name):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        last_name_text_field = self.chrome.find_elements(*self.INPUT_LAST_NAME) # pentru a returna toate elementele cu acelasi class name trebui apelat find_elements
        last_name_text_field[1].send_keys(last_name)

    def click_high_school(self):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        self.chrome.find_element(*self.RADIO_BUTTON).click()

    def click_autocomplete(self):
        self.chrome.get('https://formy-project.herokuapp.com')
        self.chrome.find_element(*self.AUTOCOMPLETE_LINK_TEXT).click()

    def click_enable_disabled(self):
        self.chrome.get('https://formy-project.herokuapp.com')
        self.chrome.find_element(*self.ENABLE_DISABLED_LINK).click()

    def input_first_name_by_xpath(self, first_name):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        self.chrome.find_element(*self.INPUT_FIRST_NAME_BY_XPATH).send_keys(first_name)



selector = Selectors()
selector.first_name_field("Robert")
from time import sleep
# sleep(3)

# selector.last_name_field("Stanescu")
# # sleep(3)
#
# selector.click_high_school()
# sleep(3)
#
# selector.click_autocomplete()
# sleep(3)
#
# selector.click_enable_disabled()
# sleep(3)


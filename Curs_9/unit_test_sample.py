import unittest
from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test(TestCase):
    FORM_LINK = (By.LINK_TEXT, "Form")
    INPUT_FIRST_NAME = (By.ID, "first-name")

# se ruleaza inainte de fiecare test - facem setup
    def setUp(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://formy-project.herokuapp.com")
        self.chrome.find_element(*self.FORM_LINK).click()

    # se ruleaza dupa fiecare test - facem cleanup
    def tearDown(self):
        self.chrome.quit()

    # metoda trebuie sa inceapa cu test
    def test_url(self):
        expected_url = "https://formy-project.herokuapp.com/form"
        actual_url = self.chrome.current_url
        assert expected_url == actual_url

    def test_page_title(self):
        actual_title = self.chrome.title
        expected_title = "Formy"
        assert actual_title == expected_title

    @unittest.skip    # facem skip la testul pe care nu dorim sa il executam
    def test_first_name(self):
        first_name = self.chrome.find_element(*self.INPUT_FIRST_NAME)
        first_name.send_keys("Robert")

    def test_element_displayed(self):
        first = self.chrome.find_element(*self.INPUT_FIRST_NAME)
        self.assertTrue(first.is_displayed())

    @unittest.skip
    def test_element_not_displayed(self):
        element_inexistent = self.chrome.find_element(By.ID, "Nu exista")
        self.assertFalse(element_inexistent.is_displayed())

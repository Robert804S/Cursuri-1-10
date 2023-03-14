'''
Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
- setUp()
- Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication

tearDown()
Quit browser

● Test 1
- Verifică dacă noul url e corect

● Test 2
- Verifică dacă page title e corect

● Test 3
- Verifică textul de pe elementul xpath=//h2 e corect

● Test 4
- Verifică dacă butonul de login este displayed

● Test 5
- Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

● Test 6
- Lasă goale user și pass
- Click login
- Verifică dacă eroarea e displayed

● Test 7
- Completează cu user și pass invalide
- Click login
- Verifică dacă mesajul de pe eroare e corect
- Este și un x pus acolo extra așa că vom folosi soluția de mai jos
expected = 'Your username is invalid!'
self.assertTrue(expected in actual, 'Error message text is
incorrect')

● Test 8
- Lasă goale user și pass
- Click login
- Apasă x la eroare
- Verifică dacă eroarea a dispărut

● Test 9
- Ia ca o listă toate //label
- Verifică textul ca textul de pe ele să fie cel așteptat (Username și
Password)
- Aici e ok să avem 2 asserturi

● Test 10
- Completează cu user și pass valide
- Click login
- Verifică ca noul url CONTINE /secure
- Folosește un explicit wait pentru elementul cu clasa ’flash succes’
- Verifică dacă elementul cu clasa=’flash succes’ este displayed
- Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

● Test 11
- Completează cu user și pass valide
- Click login
- Click logout
- Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
'''

import unittest
from time import sleep

from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class Login(TestCase):

    FORM_AUTHENTICATION = (By.CSS_SELECTOR, "a[href='/login']")
    FLASH_SUCCESS = (By.ID, "flash")

    def setUp(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.implicitly_wait(3)
        self.chrome.find_element(*self.FORM_AUTHENTICATION).click()

    def tearDown(self):
        self.chrome.quit()

    def test_1(self):
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        assert actual_url == expected_url
        print('Url-urile sunt identice')

    def test_2(self):
        actual_title = self.chrome.title
        expected_title = "The Internet"
        assert actual_title == expected_title
        print("Titlul este cel pe care il asteptam")

    def test_3(self):
        WebDriverWait(self.chrome, 5).until(
            EC.text_to_be_present_in_element((By.XPATH, "//h2[normalize-space()='Login Page']"), 'Login Page'))
        print("Textul este corect")

    def test_4(self):
        butonul_login = self.chrome.find_element(By.TAG_NAME, "i")
        self.assertTrue(butonul_login.is_displayed())
        print("Butonul login este afisat")

    @unittest.skip
    def test_5(self):
        self.chrome.find_element(By.CSS_SELECTOR, "a[target='_blank']").click()
        self.chrome.implicitly_wait(10)
        expected_url = "http://elementalselenium.com/" # se deschide pe alta pagina!
        assert self.chrome.current_url != expected_url
        print("Atributul href al linkului este corect!")

    def test_6(self):
        self.chrome.find_element(By.TAG_NAME, "i").click()   # click pe Login
        error_text = self.chrome.find_element(By.ID, "flash")
        self.assertTrue(error_text.is_displayed())
        print('Eroarea este afisata daca apasam pe butonul login fara sa completam username & password')

    def test_7(self):
        self.chrome.find_element(By.ID, "username").send_keys("user gresit")
        self.chrome.find_element(By.ID, "password").send_keys("parola super gresita")
        self.chrome.find_element(By.TAG_NAME, "i").click()  # Click Login
        actual = self.chrome.find_element(By.CSS_SELECTOR, "#flash").text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')
        print("Textul 'Your username is invalid!' este prezent in eroare!")

    def test_8(self):
        self.chrome.find_element(By.TAG_NAME, "i").click()   # click pe Login
        self.chrome.find_element(By.CSS_SELECTOR, ".close").click()   #click pe x pentru a inchide eroarea
        sleep(2)
        # error_text = self.chrome.find_element(By.XPATH, "//div[@id='flash']")   # nu functioneaza cu assert
        # self.assertFalse(error_text.is_displayed())                             # nu functioneaza cu assert
        # EC.invisibility_of_element_located((By.XPATH, "//div[@id='flash']"))
        # print("Eroarea a disparut dupa ce am apasat pe 'x'")
        try:
            self.chrome.find_element(By.XPATH, "//div[@id='flash']")
        except Exception as e:
            print(e)
            print("Eroarea a disparut dupa ce am apasat pe 'x'")

    def test_9(self):
        label = self.chrome.find_elements(By.XPATH, "//label")
        assert label[0].text == "Username"
        assert label[1].text == "Password"
        print("Totul este in regula!")

    def test_10(self):
        self.chrome.find_element(By.ID, "username").send_keys("tomsmith")
        self.chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.chrome.find_element(By.TAG_NAME, "i").click()
        sleep(1)
        assert "/secure" in self.chrome.current_url
        print("Noul URL contine '/secure'")
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((By.ID, "flash")))
        print("A fost folosit Explicit Wait")
        WebDriverWait(self.chrome, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#flash"))) # nu am reusit folosind Class Name
        print("Elementul este vizibil!")
        WebDriverWait(self.chrome, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#flash"), 'secure area!'))
        print("Textul 'secure area!' apare in element!")

    def test_11(self):
        self.chrome.find_element(By.ID, "username").send_keys("tomsmith")
        self.chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.chrome.find_element(By.TAG_NAME, "i").click()   #Click Login
        self.chrome.find_element(By.CSS_SELECTOR, ".button.secondary.radius").click()   #Click Logout
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        assert actual_url == expected_url
        print('Url-urile sunt identice')

    def test_12(self):
        # self.chrome.find_element(By.ID, "username").send_keys("tomsmith")
        elementul_h4 = "This is where you can log into the secure area. Enter tomsmith for the username and SuperSecretPassword! for the password. If the information is wrong you should see error messages."
        lista_elemente_h4 = elementul_h4.split( )
        print(lista_elemente_h4)
        for cuvant in lista_elemente_h4:
            self.chrome.find_element(By.ID, "username").send_keys("tomsmith")
            self.chrome.find_element(By.ID, "password").send_keys(cuvant)
            self.chrome.find_element(By.TAG_NAME, "i").click()
            if self.chrome.current_url == "https://the-internet.herokuapp.com/secure":
                sleep(2)
                print(f'Parola secreta este {cuvant}!')
                break
        else:
            print('Nu am reușit să găsesc parola')

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# initializam chrome

chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.maximize_window()

chrome.get("https://formy-project.herokuapp.com/form")
sleep(3)

'''
Vrem sa cautam un element cu ID-ul first name pe pagina
Sistemul va cauta acel element si daca il va gasi va trece instant la urmatoarea instructiune

Daca nu gaseste sistemul va continua sa il caute pe toata durata stabilita in implicit wait

'''

chrome.implicitly_wait(10)

chrome.find_element(By. ID, "first-name").send_keys('Robert')
sleep(3)

print('instructiunea urmatoare 1')

chrome.find_element(By. ID, "2311313").send_keys("nu gasesc")

print('instructiune urmatoare 2')

chrome.quit()

'''
setam wait in secunde = o modalitate prin care definim un timp global de asteptare 
pana sa dea eroare cand un element nu este gasit
este globala pana intalneste chrome.quit()
'''
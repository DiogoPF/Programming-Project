from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pyhtml2pdf import converter
from bs4 import BeautifulSoup
import requests
import pdfquery
import pandas as pd




option = Options()

option.add_argument("window-size=1200x600")
option.add_experimental_option("detach", True)

Avc ='AVC'

driver = webdriver.Chrome("C:\\Users\\gonca\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe", chrome_options=option)
driver.get("https://www.insa.min-saude.pt/category/informacao-e-cultura-cientifica/publicacoes/")
time.sleep(5.3)
driver.find_element(By.LINK_TEXT, 'Repositório Científico do Instituto Ricardo Jorge').click() 
time.sleep(2)
driver.execute_script("window.scrollTo(0, 800)") 
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'bulletcheck').click()
time.sleep(3.3)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'dropdown-toggle').click()
time.sleep(1.3)
driver.find_element(By.LINK_TEXT, 'Assunto').click() 
time.sleep(2.7)
driver.find_element(By.XPATH, "//*[@id='browse_navigation']/form/input[4]").send_keys(Avc)
time.sleep(1.2)
driver.find_element(By.XPATH, "//*[@id='browse_navigation']/form/input[5]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div[3]/div/ul/li[1]/a").click()

print(driver.current_url)

url = driver.current_url
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
url2 ='http://repositorio.insa.pt/'
links = []

response = requests.get(url)
# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
 
i = 0
 
# From all links check for pdf link and
# if present download file
for link in links:
    if ('/handle/' in link.get('href', [])):
        i += 1
        print("Downloading file: ", i)
 
        # Get response object for link
        response = requests.get( url2 + link.get('href'))
 
        # Write content in pdf file
        pdf = open("pdf"+str(i)+".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ", i, " downloaded")
 

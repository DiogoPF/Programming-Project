from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


option = Options()

option.add_argument("window-size=1200x600")
option.add_experimental_option("detach", True)

Var1 ='Healthy life years'

driver = webdriver.Chrome("C:\\Users\\gonca\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe", chrome_options=option)
driver.get("https://ec.europa.eu/eurostat")
time.sleep(5.3)
driver.find_element(By.XPATH, '//*[@id="input-search-_estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J_"]').send_keys(Var1) 
time.sleep(2.3)
driver.find_element(By.XPATH, '//*[@id="search-form-id-_estatsearchportlet_WAR_estatsearchportlet_INSTANCE_bHVzuvn1SZ8J_"]/button').click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 400)")
time.sleep(1.2) 
driver.find_element(By.XPATH, '//*[@id="search-results-container"]/div[2]/article[1]/div/div/div[2]/div[2]/a[1]').click()
time.sleep(8.9)
driver.find_element(By.XPATH, '//*[@id="dropdownDownload"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="xlsx__FullDownload"]').click()
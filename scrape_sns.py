import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




url = "https://www.sns.gov.pt/transparencia/"

option = Options()

option.add_argument("window-size=1200x600")
option.add_experimental_option("detach", True)

Avc ='AVC'

driver = webdriver.Chrome("C:\\Users\\gonca\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe", chrome_options=option)
driver.get(url)
time.sleep(2)
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='pesquisa']")))
time.sleep(1)
element.send_keys('Avc')
time.sleep(1)
element.send_keys(Keys.RETURN)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.find_element(By.XPATH, "//*[@id='main']/div/ods-infinite-scroll-results/div/div[1]/ods-catalog-card/div/div[1]/ods-catalog-card-description/p").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='main']/div/div[4]/div[2]/div[1]/a[5]").click()
time.sleep(1.5)
driver.find_element(By.XPATH, "//*[@id='main']/div/div[4]/div[2]/div[2]/div[8]/div/div/div/div[1]/ul[1]/li[1]/div/a").click()





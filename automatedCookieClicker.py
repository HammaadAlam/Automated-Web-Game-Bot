from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_path = '/Users/usman/Downloads/chromedriver-mac-x64 2/chromedriver'

service = Service(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service)

driver.get('https://orteil.dashnet.org/cookieclicker/')

bigCookieID = "bigCookie"
cookiesID = "cookies"
productPrice = "productPrice"
productPrefix = "product"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, bigCookieID))
)

cookie = driver.find_element(By.ID, bigCookieID)

time.sleep(10)

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookiesID).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))

    for i in range(4):
        productPrice = driver.find_element(By.ID, productPrefix + str(i)).text.replace(",", "")

        if not productPrice.isdigit():
            continue

        productPrice = int(productPrice)

        if cookies_count >= productPrice:
            product = driver.find_element(By.ID, productPrefix + str(i))
            product.click()
            break
import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
# driver.execute_script("document.body.style.zoom='80%'")
wait = WebDriverWait(driver, 30)
driver.get("https://uat-web.freetv.tv/apps/smarttv/prod-for-uat/hisense/index.html")
driver.execute_script("document.body.style.zoom='80%'")

time.sleep(8)
login_btn = driver.find_element(By.CSS_SELECTOR, ".view-login__buttons > div:nth-child(2)")
login_btn.click()
time.sleep(2)
press_on_number_1 = driver.find_element(By.CSS_SELECTOR, ".view-login__keyboard-container > div > div:nth-child(1)")
press_on_number_2 = driver.find_element(By.CSS_SELECTOR, ".view-login__keyboard-container > div > div:nth-child(2)")
press_on_number_3 = driver.find_element(By.CSS_SELECTOR, ".view-login__keyboard-container > div > div:nth-child(3)")
press_on_number_4 = driver.find_element(By.CSS_SELECTOR, ".view-login__keyboard-container > div > div:nth-child(4)")
press_on_number_5 = driver.find_element(By.CSS_SELECTOR, ".view-login__keyboard-container > div > div:nth-child(5)")
press_on_number_6 = driver.find_element(By.CSS_SELECTOR, ".view-login__keyboard-container > div > div:nth-child(6)")
press_on_number_7 = driver.find_element(By.CSS_SELECTOR, ".view-login__keyboard-container > div > div:nth-child(7)")
press_on_number_8 = driver.find_element(By.CSS_SELECTOR, ".view-login__keyboard-container > div > div:nth-child(8)")
press_on_number_9 = driver.find_element(By.CSS_SELECTOR, ".view-login__keyboard-container > div > div:nth-child(9)")


time.sleep(2)
press_on_number_4.click()
time.sleep(1)
press_on_number_8.click()
time.sleep(1)
press_on_number_1.click()
time.sleep(1)
press_on_number_2.click()
time.sleep(1)
press_on_number_3.click()
time.sleep(1)
press_on_number_4.click()
time.sleep(1)
press_on_number_5.click()
time.sleep(1)
press_on_number_6.click()
time.sleep(1)
press_on_number_7.click()
time.sleep(1)
press_on_number_8.click()
time.sleep(1)
press_on_number_9.click()
time.sleep(1)
confirm_btn = driver.find_element(By.CSS_SELECTOR, ".button.view-login__button.is-clickable.is-focused")
confirm_btn.click()
input("end")


# for number in enter_number:
#     print(number.text)
#     number.send_keys("48123465789")
#     input("end")
# enter_number.send_keys("48123456789")
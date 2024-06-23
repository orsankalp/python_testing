import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://192.168.1.2/")
driver.maximize_window()
bookingXpath = "//a[contains(@href, '/booking/')]"
clientName = "client_name"
clientPhone = "client_phone"
clientEmail = "client_email"
selectVehicle = "select_vehicle"
periodFrom = "period_from"
periodTo = "period_to"
driver.find_element(By.XPATH, bookingXpath).click()
driver.find_element(By.NAME, clientName).send_keys("Nimsha")
driver.find_element(By.NAME, clientPhone).send_keys("97565536")
driver.find_element(By.NAME, clientEmail).send_keys("orsankalp@gmail.com")
driver.find_element(By.NAME, selectVehicle).send_keys("Audi")
time.sleep(2)
driver.find_element(By.NAME, periodFrom).send_keys("19/07/2024")
driver.find_element(By.NAME, periodTo).send_keys("19/08/2024")
driver.find_element(By.CLASS_NAME, "btn-primary").click()
time.sleep(2)
success_message_element = driver.find_element(By.TAG_NAME,'strong')
actual_message = success_message_element.text
expected_message = 'Success555!'
assert expected_message == actual_message, f"Expected message: '{expected_message}', but got: '{actual_message}'"
time.sleep(2)
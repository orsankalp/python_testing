import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pythonFramework.BaseTest import BaseTest


@pytest.mark.usefixtures("setup")
class TestOne(BaseTest):
    def test_Booking(self):
        log = self.getLogger()
        bookingXpath = "//a[contains(@href, '/booking/')]"
        clientName = "client_name"
        clientPhone = "client_phone"
        clientEmail = "client_email"
        selectVehicle = "select_vehicle"
        periodFrom = "period_from"
        periodTo = "period_to"
        log.info("clicking on the Booking icon")
        self.driver.find_element(By.XPATH, bookingXpath).click()
        self.driver.find_element(By.NAME, clientName).send_keys("Nimsha")
        log.info("passed the name")
        self.driver.find_element(By.NAME, clientPhone).send_keys("97565536")
        log.info("passed the phone number")
        self.driver.find_element(By.NAME, clientEmail).send_keys("orsankalp@gmail.com")
        log.info("passed the email")
        self.driver.find_element(By.NAME, selectVehicle).send_keys("Audi")
        log.info("passed the carname")
        time.sleep(2)
        self.driver.find_element(By.NAME, periodFrom).send_keys("19/07/2024")
        log.info("passing the datefrom")
        self.driver.find_element(By.NAME, periodTo).send_keys("19/08/2024")
        log.info("passing the dateto")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "btn-primary").click()
        log.info("clicking submit")
        time.sleep(2)
        success_message_element = self.driver.find_element(By.TAG_NAME, 'strong')
        actual_message = success_message_element.text
        expected_message = 'Success555!'
        assert expected_message == actual_message, f"Expected message: '{expected_message}', but got: '{actual_message}'"
        time.sleep(2)
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pythonFramework.BaseTest import BaseTest


class TestContactus(BaseTest):

    def test_contact_us(self):
        log = self.getLogger()
        contactXpath = "//a[contains(@href, '/contact/')]"
        clientid = "1234"
        clientphone = "9877656778"
        clientproblem = "tyre problem"
        log.info("clicking on the Booking icon")
        self.driver.find_element(By.XPATH, contactXpath).click()
        self.driver.find_element(By.NAME, "client_id").send_keys(clientid)
        log.info("passed the Clientid")
        self.driver.find_element(By.NAME, "client_phone").send_keys(clientphone)
        log.info("passed the phone number")
        self.driver.find_element(By.NAME, "client_problem").send_keys(clientproblem)
        log.info("passed the carproblem")
        self.driver.find_element(By.CLASS_NAME, "btn-primary").click()
        log.info("clicking submit")
        success_message_element = self.driver.find_element(By.TAG_NAME, 'strong')
        actual_message = success_message_element.text
        expected_message = 'Success!'
        assert expected_message == actual_message, f"Expected message: '{expected_message}', but got: '{actual_message}'"
        time.sleep(2)

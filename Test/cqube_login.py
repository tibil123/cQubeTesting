import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Data.Paramters import Data
from get_dir import pwd


class CqubeLogin(unittest.TestCase):
    def setUp(self):
        p = pwd()
        self.driver = p.get_chrome_headless_driver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.URL)

    def test_search(self):
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()

    def tearDown(self):
        self.driver.close()

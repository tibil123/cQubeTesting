import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class pwd():

    def get_system_path(self):
        pwd = os.path.dirname(__file__)
        return pwd

    def get_report_path(self):
        cwd = os.path.dirname(__file__)
        report_path = os.path.join(cwd, 'Reports/report.html')
        return report_path



    def get_driver_path(self):
        cwd = os.path.dirname(__file__)
        return os.path.join(cwd,'Driver/geckodriver')

    def get_firefox_driver(self):
        p = pwd()
        driver = webdriver.Firefox(executable_path=p.get_driver_path())
        return driver

    def get_chrome_headless_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        p=pwd()
        driver=webdriver.Chrome(chrome_options=options,executable_path=p.get_driver_path())
        return driver

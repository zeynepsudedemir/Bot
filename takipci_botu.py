from selenium import webdriver
from get_user import password,username
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Instagram():
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver=webdriver.Chrome()

    def kullanici_giris(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        username=self.driver.find_element(By.NAME,"username").send_keys(self.username)
        password=self.driver.find_element(By.NAME,"password").send_keys(password)
        time.sleeep(2)

        self.driver.find_element(By.CSS_SELECTOR,'button [type="submit"]')
        time.sleeep(2)



insta=Instagram(username,password)
insta.kullanici_giris()
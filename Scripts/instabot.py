import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


class BotInsta:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        time.sleep(5)

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(3)
        input_username = self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        time.sleep(3)
        input_password = self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        time.sleep(3)
        input_submit = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="button"]').click()
        time.sleep(3)

    def like(self, url):
        self.driver.get(url)
        time.sleep(3)
        firstpost = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/p/CqDMPTooUXh/"]').click()
        time.sleep(3)
        for i in range(1, 10):
            if self.driver.find_elements(By.CSS_SELECTOR, 'svg[aria-label="Unlike"]'):
                time.sleep(3)
                self.driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Next"]').click()
                time.sleep(3)
            elif self.driver.find_elements(By.CSS_SELECTOR, 'svg[aria-label="Like"]'):
                time.sleep(2)
                self.driver.find_elements(By.CSS_SELECTOR, 'svg[aria-label="Like"]')[1].click()
                time.sleep(3)
                LIKES = self.driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Next"]').click()
                time.sleep(3)
    def comment(self,url):
        self.driver.get(url)
        time.sleep(5)
        posts= self.driver.find_elements(By.CSS_SELECTOR, 'div._aa8k a')
        posts[0].click()
        time.sleep(2)
        for i in range(1,10):
            self.driver.find_elements(By.CSS_SELECTOR, 'svg[aria-label="Comment"]')[1].click()
            time.sleep(2)
            comment = self.driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Add a comment…"]').send_keys('prefect :))'+Keys.ENTER)
            time.sleep(2)
            LIKES = self.driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Next"]').click()
            time.sleep(5)

    def follower(self,url):
        self.driver.get(url)
        time.sleep(5)
        btns=self.driver.find_elements(By.TAG_NAME,'li')
        btns[1].click()
        time.sleep(5)
        followers=self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button').click()
        # for item in range(1,10):
        #     followers[i].click()
        #     time.sleep(3)
        time.sleep(3)





bot = BotInsta('username', 'password')

bot.login()
bot.follower('https://www.instagram.com/donya/')
time.sleep(10)

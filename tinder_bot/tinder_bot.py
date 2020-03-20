from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class bot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get('www.tinder.com')

    def loop(self):
        while True:
            self.driver.implicitly_wait(10)
            sleep(2)
            button1 = self.driver.find_element_by_xpath('//*[@id="poll-answer-2073"]')
            button1.click()
            sleep(1)
            button2 = self.driver.find_element_by_xpath('//*[@id="polls-43-ans"]/p[1]/input')
            button2.click()
            sleep(1)
            self.driver.refresh()

bot = bot()
bot.loop()

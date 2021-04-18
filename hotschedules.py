import time

import pandas as pd
from selenium import webdriver

from secrets import hot_user, hot_pass

option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                          options=option)
driver.implicitly_wait(30)
df = pd.DataFrame()
def hot_login():
    driver.get('https://app.hotschedules.com/hs/login.jsp?_ga=2.80431063.1749537157.1572278369-1299434720.1568126387')
    driver.find_element_by_xpath('//*[@id="loginusername"]').send_keys(hot_user)
    driver.find_element_by_xpath('//*[@id="loginpassword"]').send_keys(hot_pass)
    driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
    # time.sleep(3)
    driver.find_element_by_xpath('//*[@id="stores_chosen"]/a/div').click()
    driver.find_element_by_xpath('//*[@id="stores_chosen"]/div/ul').click()


def schedules():
    hot_login()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="GlobalNav"]/div[2]/div[1]/div/div[1]/div').click()
    driver.find_element_by_xpath('//*[@id="GlobalNav"]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/ul/li[6]/a').click()

    v = driver.find_elements_by_xpath('//*[@id="DataTables_Table_0"]/tbody')
    z = driver.find_elements_by_class_name('employee-cell sorting_2 ui-droppable')

    for z in v:
        u = z.text


def add_sched():
    hot_login()
    time.sleep(5)


schedules()

time.sleep(10)
driver.quit()

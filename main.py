from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import unittest
import time

browser = webdriver.Firefox()
browser.get('https://noc-new.is74.ru')



def autorization():
    browser.find_element_by_name("username").send_keys('')
    browser.find_element_by_name("password").send_keys('')
    browser.find_element_by_name("yt0").click()
    browser.get('https://noc-new.is74.ru/damage/main/index.html?STATE=damage&AREA_SET_ID%5B0%5D=1&CATEGORY%5B0%5D=0&CATEGORY%5B1%5D=1&CATEGORY%5B2%5D=2&Timeline%5BDATE%5D=%D0%A1%D0%B5%D0%B9%D1%87%D0%B0%D1%81&Timeline%5BTOTAL_SIZE%5D=auto&Timeline%5BREFRESH_RATE%5D=0&pagesize=5')
def damage():
    browser.find_element_by_id('checkuncheckall').click()
    browser.find_element_by_id('action').click()
    select = Select(browser.find_element_by_id('action'))
    select.select_by_visible_text('Массово редактировать')
    browser.find_element_by_id('Damage_takeSelf').click()
    browser.find_element_by_link_text('Устранение аварии').click()
    browser.find_element_by_id('executorsselect_AUTO').send_keys('Громов')
    time.sleep(1)
    browser.find_element_by_id('executorsselect_AUTO').send_keys(Keys.ARROW_DOWN + Keys.ENTER)
    browser.find_element_by_id('chief-executor-add').click()
    browser.find_element_by_id('mainsubmit').click()

autorization()
damage()
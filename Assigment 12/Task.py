from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search():
    driver = webdriver.Safari()

    driver.get("https://www.google.com")
    driver.maximize_window()

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("selenium")
    search_box.send_keys(Keys.ENTER)

    time.sleep(5)
    driver.quit()

    button = driver.find_element(By.NAME, "btnK")
    button.click()

def auto():
    driver = webdriver.Safari()

    driver.get("https://www.google.com")
    driver.maximize_window()

    input = driver.find_element(By.NAME, "q")
    input.send_keys("selenium")
    time.sleep(5)
    button = driver.find_element(By.NAME, "btnK")
    button.click()
    time.sleep(5)
    driver.back()
    time.sleep(5)
    driver.forward()
    time.sleep(5)
    driver.quit()

def met():
    driver = webdriver.Safari()
    driver.get("https://www.google.com")
    driver.maximize_window()
    input = driver.find_element(By.NAME, "q")
    input.send_keys("selenium")
    time.sleep(5)
    button = driver.find_element(By.NAME, "gN089b")
    button.click()

def link():
    driver = webdriver.Safari()
    driver.get("https://www.amazon.com")
    driver.maximize_window()
    time.sleep(5)
    select = driver.find_element(By.LINK_TEXT, "Best Sellers")
    select.click()
    select_1 = driver.find_element(By.PARTIAL_LINK_TEXT, "Audio")
    select_1.click()

def refresh():
    driver = webdriver.Safari()
    driver.get("https://www.amazon.com")
    driver.maximize_window()
    time.sleep(5)
    driver.refresh()

def xpath():
    driver = webdriver.Safari()
    driver.get("https://www.amazon.com")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("iphones")
    driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()

def data():
    driver = webdriver.Safari()
    driver.get("https://www.amazon.com")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("iphones")
    driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
    list = driver.find_element(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
    print(str(len(list)) + ' products found')
    for i in list:
        print(i.text)
    driver.quit()



search()
auto()    
met()
link()
refresh()
xpath()
data()
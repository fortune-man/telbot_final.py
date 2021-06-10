from selenium import webdriver
from selenium.webdriver.common.by import By
import time
opts = webdriver.ChromeOptions()
opts.add_argument('window-size=960,750')
def usafood(bot, chat_id):
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.implicitly_wait(10)
    driver.get('http://dogumaster.com/select/menu')
    meal = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[1]/label[2]')
    usa_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[5]')
    usa_food.click()
    Alone_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[3]/label[2]')
    Alone_food.click()
    randomMenu_click = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[5]')
    randomMenu_click.click()
    time.sleep(1.5)
    result = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text
    bot.send_message(chat_id, text="오늘은 " + result + " 을(를) 추천드릴게요.")
    driver.quit()
    return result
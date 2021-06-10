from selenium import webdriver
from selenium.webdriver.common.by import By
def social_pack(bot, chat_id):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://news.naver.com')
    tit = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').text
    tit2 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').text
    tit3 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').text
    tit4 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[4]/div[1]/a').text
    tit5 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[5]/div[1]/a').text
    soci = f'네이버 사회뉴스 탑 5 소개해드릴게요. \n 1.{tit},\n 2.{tit2},\n 3.{tit3}, \n 4.{tit4},\n 5.{tit5}'
    driver.quit()
    bot.send_message(chat_id, soci)
    return soci
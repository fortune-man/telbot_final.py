import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def corona_pack(bot, chat_id):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun=')
    route = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/div/table/tbody').text
    time.sleep(1)
    driver.get('https://m.news.naver.com/covid19/index.nhn')
    add1 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[6]/div[3]/div/ul/li[1]').text
    add2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[6]/div[3]/div/ul/li[2]').text
    add3 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[6]/div[3]/div/ul/li[3]').text
    stt= driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[3]/div[2]/div[1]/dl').text
    covd = f'코로나 환자 신규 합계 {stt} \n 확진자 이동경로 \n{route}, \n실시간 추가 확진 현황{add1}+{add2}+{add3}'
    bot.send_message(chat_id, covd)
    driver.quit()
    return covd

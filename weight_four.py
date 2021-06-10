from selenium import webdriver
from selenium.webdriver.common.by import By


def bp_pack(health_result,bot,chat_id):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=105&cal_type=E')
    bnp = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
    bp_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다.\n{bnp}'
    driver.quit()
    bot.send_message(chat_id, bp_info)
    return bp_info
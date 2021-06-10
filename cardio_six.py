from selenium import webdriver
from selenium.webdriver.common.by import By


def rn_pack(health_result,bot,chat_id):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=77&cal_type=E')
    run = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
    rn_info = f'야외에서 할 수 있는 유산소 운동 중 {health_result}를 추천합니다. 달리기는 {run}'
    driver.quit()
    bot.send_message(chat_id, rn_info)
    return rn_info
from selenium import webdriver
from selenium.webdriver.common.by import By


def pu_pack(health_result,bot,chat_id):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=451&cal_type=E')
    pus = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
    pu_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다.\n{pus}' 
    driver.quit()
    bot.send_message(chat_id, pu_info)
    return pu_info
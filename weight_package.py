from selenium import webdriver
from selenium.webdriver.common.by import By


def weight_pack(health_result,bot,chat_id):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=451&cal_type=E')
    cardiohealth = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
    cardiohealth_info = f'실내에서 할 수 있는 유산소 운동 중  {health_result}를 추천합니다.\n{cardiohealth}'
    driver.quit()
    bot.send_message(chat_id, cardiohealth_info)
    return cardiohealth_info
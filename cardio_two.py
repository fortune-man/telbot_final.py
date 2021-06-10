from selenium import webdriver
from selenium.webdriver.common.by import By


def str_pack(health_result,bot,chat_id):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=21&cal_type=E')
    stair = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
    str_info = f'실내에서 할 수 있는 유산소 운동 중  {health_result}를 추천합니다.\n{stair}'
    driver.quit()
    bot.send_message(chat_id, str_info)
    return str_info
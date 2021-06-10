from selenium import webdriver
from selenium.webdriver.common.by import By


def bf_info(health_result,bot,chat_id):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=491&cal_type=E')
    buf = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
    bf_info = f'실내에서 할 수 있는 유산소 운동 중  {health_result}를 추천합니다.\n{buf}'
    driver.quit()
    bot.send_message(chat_id, bf_info)
    return bf_info
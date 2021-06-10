from selenium import webdriver
from selenium.webdriver.common.by import By


def wk_pack(health_result,bot,chat_id):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=14&cal_type=E')
    walk = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
    wk_info = f'야외에서 할 수 있는 유산소 운동 중 {health_result}운동을 추천합니다. 걷기 운동 효과 {walk}'
    driver.quit()
    bot.send_message(chat_id, wk_info)
    return wk_info
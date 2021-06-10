from selenium import webdriver
from selenium.webdriver.common.by import By


def bc_pack(health_result,bot,chat_id):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=254&cal_type=E')
    bic = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
    bc_info = f' 야외에서 할 수 있는 유산소 운동 중 {health_result}운동을 추천합니다.\n{bic}'
    driver.quit()
    bot.send_message(chat_id, bc_info)
    return bc_info
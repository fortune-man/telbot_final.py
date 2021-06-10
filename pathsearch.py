from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def path(result,bot,chat_id):
    keyword = result
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get(f'https://www.diningcode.com/isearch.php?query={keyword}')
    location = driver.find_element(By.XPATH,'//*[@id="contents"]/div[1]/div/img')
    action_loc = webdriver.ActionChains(driver)
    action_loc.move_to_element(location)
    action_loc.click() # 내 위치 업데이트
    action_loc.perform() #action함수 실행
    time.sleep(0.3)
    shop = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[1]').text.split('.')
    score = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/p[3]')
    voice1 = f'내 주변 {keyword} 맛집검색결과:\n맛집 점수 {score.text}, 상위{shop[0]}순위 {shop[1]}입니다.\n이동경로를 안내해드릴게요.\n'
    destination = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[3]')
    dt = destination.text # 목적지, 맛집주소
    driver.get('https://map.kakao.com/') # 맛집 길찾기 시작
    time.sleep(0.5)
    direction = driver.find_element(By.XPATH,'//*[@id="search.tab2"]/a')
    box = driver.find_element(By.XPATH,'/html/body/div[10]/div/div/img')
    action_box = webdriver.ActionChains(driver)
    action_box.move_to_element(box)
    action_box.click()
    action_box.perform()
    direction.click()
    startpoint = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input0"]')
    ds = '서울특별시 강동구 천호동 432-11' # 대신it학원 주소
    action_start = webdriver.ActionChains(driver)
    action_start.move_to_element(startpoint)
    action_start.click()
    action_start.perform()
    startpoint.send_keys(ds, Keys.ENTER) # 출발지입력
    time.sleep(0.5)
    des = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
    des.send_keys(dt, Keys.ENTER) # 목적지입력
    time.sleep(0.5)
    public_tr = driver.find_element(By.XPATH, '//*[@id="transittab"]')
    public_tr.click()
    time.sleep(1)
    no_pass = driver.find_elements(By.XPATH, '//*[@id="info.flagsearch"]/div[7]/div/div[1]/h3')
    if len(no_pass) == 0:
        pub_time = driver.find_element(By.XPATH, '//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[1]')
        pub_info = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[2]')
        voice3 = f'대중교통 이용시 예상소요시간 {pub_time.text}, {pub_info.text}. 교통카드를 챙겨주세요.\n'
    else:
        voice3 = "대중교통 경로가 없습니다."
        pass
    walk = driver.find_element(By.XPATH, '//*[@id="walktab"]')
    walk.click()
    time.sleep(1)
    walk_fast_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    walk_fast_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    walk_slow_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    walk_slow_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    voice4 = f'도보 이용시 최단거리는 {walk_fast_time.text}, {walk_fast_dis.text}, 편안한 길은 {walk_slow_time.text}, {walk_slow_dis.text}\n'
    x = voice1 + voice3 + voice4
    screen = driver.find_element_by_class_name("cont_map")
    element_png = screen.screenshot_as_png
    with open('test.png', 'wb') as file:
        file.write(element_png)
    driver.quit()
    bot.send_photo(chat_id, element_png)
    bot.send_message(chat_id, x)
    return x

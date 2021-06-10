from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def weather(bot, chat_id):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.google.com/search?q=오늘날씨')
    time.sleep(0.5)
    weather= driver.find_element(By.XPATH,'//*[@id="wob_dc"]')
    weather_info = weather.text
    svg = driver.find_element(By.XPATH,'//*[@id="wob_gsvg"]')
    tmp_list = svg.text.split('\n')
    map_list = list(map(float, tmp_list))
    tmp_max = max(map_list)
    tmp_min = min(map_list)
    tmp_gap = float(tmp_max) - float(tmp_min)
    tmp_avg = sum(map_list)/len(map_list)
    voice_tmp = f'오늘의 날씨정보는 {weather_info}, 최고기온 {tmp_max}도,최저기온 {tmp_min}도,평균기온 {tmp_avg}도, 일교차는{tmp_gap}도 입니다.\n'    
    v_w_info =""
    voice_tmp_gap= ""
    voice_cl = ""

    if weather_info == '광역성 소나기':
        v_w_info1 = f'{weather_info}가 예정되어 있습니다. 휴대용 우산을 챙겨주세요.\n'
        v_w_info = v_w_info1
    elif weather_info == '비':
        v_w_info2 = f'{weather_info}가 예정되어 있습니다. 우산을 챙겨주세요.\n'
        v_w_info = v_w_info2

    if tmp_gap > 7.5:
        voice_tmp_gap1 = f'오늘은 일교차가 큽니다. 얇은 옷을 겹쳐입거나 외투를 준비해주세요.\n'
        voice_tmp_gap = voice_tmp_gap1
    else:
        voice_tmp_gap2 = f'오늘은 일교차가 크지 않습니다.\n'
        voice_tmp_gap = voice_tmp_gap2

    if tmp_avg >= 10 and tmp_avg <=16:
        voice_cl1 = f'기온별 옷차림 추천, 평균 {tmp_avg}도에는 자켓, 셔츠, 가디건, 간절기 야상, 살구색 스타킹을 추천드릴게요!'
        voice_cl = voice_cl1
    elif tmp_avg > 16 and tmp_avg <= 19:
        voice_cl2 = f'기온별 옷차림 추천, {tmp_avg}도에는 니트, 가디건, 후드티, 맨투맨, 청바지, 면바지, 슬랙스, 원피스을 추천드릴게요!'
        voice_cl = voice_cl2
    elif tmp_avg >19 and tmp_avg <=  22:
        voice_cl3 = f'기온별 옷차림 추천, {tmp_avg}도에는 긴팔티, 가디건, 후드티, 면바지 ,슬랙스, 스키니을 추천드릴게요!'
        voice_cl = voice_cl3
    elif tmp_avg >22 and tmp_avg <= 26:
        voice_cl4 = f'기온별 옷차림 추천, {tmp_avg}도에는 반팔, 얇은 셔츠, 얇은 긴팔, 반바지, 면바지을 추천드릴게요!'
        voice_cl = voice_cl4
    elif tmp_avg > 26:
        voice_cl5 = f'기온별 옷차림 추천, {tmp_avg}도에는 나시티, 반바지, 민소매, 원피스을 추천드릴게요!'
        voice_cl = voice_cl5
    elif tmp_avg < 10:
        voice_cl6 = f'기온별 옷차림 추천, {tmp_avg}도에는 패딩점퍼, 코트, 야상, 목도리, 장갑, 히트텍을 추천드릴게요!'
        voice_cl = voice_cl6

    weather_message = voice_tmp + v_w_info + voice_tmp_gap + voice_cl
    bot.send_message(chat_id, weather_message)
    driver.quit()
    return weather_message
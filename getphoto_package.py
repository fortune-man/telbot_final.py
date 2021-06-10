import os
from PIL import Image
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#집   : C:/Users/82103/Desktop/python/조별과제/foodPhoto
#학원 : C:/Users/ds_a/Desktop/python/조별과제/foodPhoto
def getphoto(result,bot,chat_id):
    driver= webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.google.com/')
    input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search.clear()
    input_search.send_keys(result, Keys.ENTER)
    food_image_search = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div//*[text()="이미지"]')
    food_image_search.click()
    food_image_choice = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    food_image = food_image_choice.get_attribute('src')
    img_folder = 'C:/Users/82103/Desktop/python/조별과제/foodPhoto'
    if not os.path.isdir(img_folder):
        os.mkdir(img_folder)
    urllib.request.urlretrieve(food_image, img_folder+'test.jpg')
    food_Photo = Image.open(img_folder+'test.jpg')
    bot.send_photo(chat_id, food_Photo.resize((120,120)))
    driver.quit()
    return food_Photo
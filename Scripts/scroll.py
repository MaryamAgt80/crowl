import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time


driver=webdriver.Chrome()
driver.get('https://www.digikala.com/search/category-motorbike/')
driver.maximize_window()
time.sleep(3)
end_scroll=driver.execute_script('return document.body.scrollHeight')


while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(2)
    now_loc=driver.execute_script('return document.body.scrollHeight')
    if now_loc == end_scroll:
        break
    end_scroll=now_loc
time.sleep(2)
images_tag=driver.find_elements(By.CSS_SELECTOR,'div.product-list_ProductListpagesContainerzAhrX.product-list_ProductListpagesContainer--withSidebar17nz1 img')
x=0
for img_tag in images_tag:
    print(img_tag.get_attribute('src'))
    name='image'+str(x)+'.jpg'
    x+=1
    with requests.get(img_tag.get_attribute('src'),stream=True) as r:
        with open(name,'wb') as f:
            for pic in r.iter_content(chunk_size=1024):
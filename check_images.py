from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import datetime


browser = webdriver.Chrome

url = "https://graceful-sunburst-78f35d.netlify.app/www.classcentral.com/index.html"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)


urllistesi=[url]
say=1
for url in urllistesi:
    urllib.request.urlretrieve(url,"Resim"+str(say)+".png")
    say +=1



# photos = driver.find_element(By.XPATH,"/html/body/div[1]/main/section[1]/div[1]/img")
# for photo in photos:
#     try:
#         image = driver.find_element(By.TAG_NAME,"img").get_attribute('src')
#         urllib.request.urlretrieve(image,"image/{}.jpg".format(datetime.datetime.now()))
#     except:
#         print("Hata Oluştu")


while True:
    continue
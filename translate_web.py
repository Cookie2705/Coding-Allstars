from translate import Translator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import googletrans


import time

browser = webdriver.Chrome

url = "https://graceful-sunburst-78f35d.netlify.app/www.classcentral.com/index.html"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

input = driver.find_elements(By.CLASS_NAME,'sticky-footer')

for i in input:
    if len(i.text) > 0:
        # print("************")
        # print(i.text)
        # print("************")
        txtFile = "deneme.txt"
        theText = i.text
        f = open(txtFile,"w",encoding="utf-8")
        f.writelines(theText)
        f.close()
        

file = open("deneme.txt","r",encoding="utf-8")

liste = file.readlines() 

for i in liste:
    try:
        translator = Translator(from_lang="Hindi",to_lang="en")
        translation = translator.translate(i)
        print (i)
        print(translation)
        print("******************************************")
    except RuntimeError:
        print(i)

while True:
     continue



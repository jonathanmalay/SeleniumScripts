
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
 

def isInFile(name , file):
    for line in file.readlines():
        if name == line:
            return True
    return False


PATH = '/home/jonathan/Desktop/tools/chromedriver'
 
 
url = 'https://easy.co.il/?q=%D7%97%D7%A0%D7%95%D7%99%D7%95%D7%AA+%D7%A6%D7%99%D7%9C%D7%95%D7%9D'

driver = webdriver.Chrome(executable_path= PATH)
driver.get(url)
 
f = open('meni.txt' , 'r+')
while True:
    try:
        all_paragraphs = driver.find_elements_by_xpath("//p[@class='biz-list-name']")
        for p in all_paragraphs:
            if not isInFile(p.text , f):
                f.write(p.text+'\n')      
        driver.execute_script("window.scrollTo(0,20000)")
        sleep(2)
        moreBtn = driver.find_element_by_xpath('//*[@class="next-page-button"]')
        moreBtn.click()
        driver.execute_script("window.scrollTo(0,20000)")
    except:
        break
   
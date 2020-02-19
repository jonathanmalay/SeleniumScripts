
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
 
 
def generateFullName():
    fnames = [('ron' , 'רון') , ('moshe' , 'משה'), ('liav' , 'ליאב'), ('roy', 'רוי')
              , ('noa' , 'נועה') , ('hila', 'הילה'), ('carmel' , 'כרמל'),
              ('carmel' , 'כרמל'), ('carmel' , 'כרמל')
              , ('carmel' , 'כרמל'), ('carmel' , 'כרמל'), ('carmel' , 'כרמל'), ('carmel' , 'כרמל'), ('daniel', 'דניאל'), ('ido', 'עידו')
              , ('rom', 'רום'), ('nadav', 'נדב'), ('yarin', 'ירין'), ('libar', 'ליבר'), ('sally', 'סאלי'), ('ziv', 'זיו')]
    lnames = [('cohen', 'כהן'), ('levi', 'לוי'), ('levy', 'לוי'), ('sher', 'שר'), ('anav', 'ענב'), ('perah', 'פרח'), ('tzubery', 'צוברי')]
    return random.choice(fnames), random.choice(lnames)
 
def createPhone():
    return '05' + str(random.randint(0,5)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
 
def Birthday():
    day = random.randint(1,28)
    if day < 10 :
        day  = '0' + str(day)
    else:
        day = str(day)
    mount = random.randint (1,12)
    if mount < 10:
        mount = '0' + str(mount)
    else:
        mount = str(mount)
    year = '2002'
        
    return mount+day+year  
  
def createEmail(firstName  , lastName):
    mail_list = ['walla.co.il' , 'gmail.com' , 'yahoo.com' , 'hotmail.com']
    temp = str(firstName) + str(lastName) + str(random.randint(1 , 9999)) + '@' + str(random.choice(mail_list))
    #print('[+] The email ---- {0} ---- is generated...'.format(temp))
    return temp
PATH = '/home/jonathan/Desktop/tools/chromedriver'
 
 
count = 0
url = 'https://docs.google.com/forms/d/e/1FAIpQLScXmXPr2iqrnLK_jKpS0qFLsRAJ74nSJU2XiYbK7-6KFR46ZQ/viewform?usp=sf_link'
while True:
    fname , lname = generateFullName()
    user_email = createEmail(fname[0], lname[0])
    fullUserName = str(fname[1]) + ' ' + str(lname[1])
    driver = webdriver.Chrome(executable_path= PATH)
    driver.get(url)
 
    email = driver.find_element_by_name('emailAddress')
 
    email.send_keys(user_email)
    sleep(0.1)
    i  = random.randint(0,1)
 
    yudBet1 = driver.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(2) > div > div:nth-child(2) > div > span > div > div:nth-child(1) > label > div > div.appsMaterialWizToggleRadiogroupElContainer.exportContainerEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
 
 
    yudbet12 = driver.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(2) > div > div:nth-child(2) > div > span > div > div:nth-child(2) > label > div > div.appsMaterialWizToggleRadiogroupElContainer.exportContainerEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
    sleep(0.1)
    if i == 0:
        yudBet1.click()
    else:
        yudbet12.click()
    sleep(0.1)
    fullName = driver.find_element_by_name('entry.1435260940')
 
    fullName.send_keys(fullUserName)
 
    driver.execute_script("window.scrollTo(0,500)")
 
    sleep(1)
    j = random.randint(0,1)
    female = driver.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(4) > div > div:nth-child(2) > div > span > div > div:nth-child(1) > label > div > div.appsMaterialWizToggleRadiogroupElContainer.exportContainerEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
 
    male = driver.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewItemList > div:nth-child(4) > div > div:nth-child(2) > div > span > div > div:nth-child(2) > label > div > div.appsMaterialWizToggleRadiogroupElContainer.exportContainerEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
    if j ==0:
        male.click()
    else:
        female.click()
 
    sleep(0.1)
 
   
    birthday = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div/div[2]/div[1]/div/div[1]/input')
 
    birthday.send_keys(Birthday())
    sleep(0.1)
    parentName = driver.find_element_by_name('entry.1693450474')
    pname , plast = generateFullName()
 
    parentName.send_keys(pname[1] + ' '+ plast[1])
    driver.execute_script("window.scrollTo(0,500)")
 
    sleep(0.1)
    parentPhoneNumber = driver.find_element_by_name('entry.1704712131')
    parentPhoneNumber.send_keys(createPhone())
    sleep(0.1)
    driver.execute_script("window.scrollTo(0,500)")
    selfPhoneNumber = driver.find_element_by_name('entry.868780705')
 
    selfPhoneNumber.send_keys(createPhone())
    sleep(0.1)
    submitBTN = driver.find_element_by_css_selector('#mG61Hd > div > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div > span')
    submitBTN.click()

    driver.close()
    count+=1
    strmessage = str('[+]----spam number = {} ------[+]'.format(count))
    print(strmessage)
#imports
from selenium import webdriver
import time
from bs4 import BeautifulSoup

#opening browser
browser = webdriver.Chrome()
browser.get('https://bioportal.bioontology.org/ontologies/MEDDRA/?p=classes')
time.sleep(3)

img = browser.find_element_by_class_name("folder-close").find_element_by_class_name("trigger")

folder_close = browser.find_elements_by_class_name("folder-close")

while True:
    if folder_close:
        img.click()
        time.sleep(2)
        browser.execute_script("arguments[0].scrollIntoView(true);", img)
        folder_close = browser.find_elements_by_class_name("folder-close")
        if folder_close:
            img = browser.find_element_by_class_name("folder-close").find_element_by_class_name("trigger")
        else:
            folder_close_last = browser.find_elements_by_class_name("folder-close-last")
            if folder_close_last:
                img = browser.find_element_by_class_name("folder-close-last").find_element_by_class_name("trigger")
                browser.execute_script("arguments[0].scrollIntoView(true);", img)
                img.click()
                time.sleep(2)
            else:
                break



#giving time to execute js
time.sleep(10)


#getting source
page = browser.page_source

#passing the page to bs4
soup = BeautifulSoup(page , 'lxml')
name = []


i = 0


#finding all contents of Inverse of SIB
while True:
    text = soup.find_all('a',{"class":"ajax-modified-cls"})[i].text
    if "http" in text:
        break
    name.append(text)
    i = i + 1


#printing the contents
for i in name:
    print(i)

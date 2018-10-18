#imports
from selenium import webdriver
import time
from bs4 import BeautifulSoup

#opening browser
browser = webdriver.Chrome()
browser.get('https://bioportal.bioontology.org/ontologies/MEDDRA/?p=classes')
time.sleep(3)


img2 = browser.find_element_by_class_name("folder-close").find_element_by_class_name("trigger")


while img2:
    img2.click()
    browser.execute_script("arguments[0].scrollIntoView(true);", img2)
    time.sleep(3)
    img2 = browser.find_element_by_class_name("folder-close").find_element_by_class_name("trigger")


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

#imports
from selenium import webdriver
import time
from bs4 import BeautifulSoup


#opening browser
browser = webdriver.Chrome()
browser.get('https://bioportal.bioontology.org/ontologies/MEDDRA/?p=classes')


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


#exiting the browser
browser.quit()


#printing the contents
for i in name:
    print(i)

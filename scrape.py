import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

ilce = pd.DataFrame(columns=['mahalle', 'sokak', 'yil', 'rayic'])
driver = webdriver.Chrome('./chromedriver')
ilcerowslist = []
for i in range(2, 47):
    mahallerowslist = []
    mahalle_adi = ''
    for j in range(1, 16):
        driver.get("https://www.turkiye.gov.tr/beyoglu-belediyesi-arsa-rayic")
        driver.find_element_by_xpath('//*[@id="mahalle"]/option[' + str(i) + ']').click()
        driver.find_element_by_xpath('//*[@id="yil"]/option['+str(j)+']').click()
        driver.find_element_by_xpath('//*[@id="mainForm"]/div/input[1]').send_keys("\n")
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contentStart"]/div/div/table/tbody')))
        body = driver.find_element_by_xpath('//*[@id="contentStart"]/div/div/table/tbody')
        rows = body.find_elements_by_tag_name('tr')
        print(len(rows))
        for k in range(len(rows)):
            fields = rows[k].find_elements_by_tag_name('td')
            dict_ = {'mahalle': fields[0].text, 'sokak': fields[1].text, 'yil': fields[2].text, 'rayic': float(fields[3].text.replace(',', '.'))}
            dict__ = {'sokak': fields[1].text, 'yil': fields[2].text, 'rayic': float(fields[3].text.replace(',', '.'))}
            mahalle_adi = fields[0].text
            mahallerowslist.append(dict__)
            ilcerowslist.append(dict_)
            if ((k % 20) == 19) and (k < len(rows) - 1):
                driver.find_element_by_class_name('next').send_keys("\n")
                myElem = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="contentStart"]/div/div/table/tbody')))
                body = driver.find_element_by_xpath('//*[@id="contentStart"]/div/div/table/tbody')
                rows = body.find_elements_by_tag_name('tr')
    mahalle = pd.DataFrame(mahallerowslist)
    mahalle.to_csv('beyoglu/'+mahalle_adi+'.csv')
ilce = pd.DataFrame(ilcerowslist)
ilce.to_csv('beyoglu.csv')
#url = "https://www.turkiye.gov.tr/beyoglu-belediyesi-arsa-rayic"
#parameters = {'mahalle': '161', 'yil': '2020'}
#r = requests.post("https://www.turkiye.gov.tr/beyoglu-belediyesi-arsa-rayic?submit", data=parameters)
#doc = BeautifulSoup(r.text, 'html.parser')
#row_tags = doc.find_all('tr')
#for row in row_tags[:5]:
#    print(row.text.strip())
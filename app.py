###P127

#beautiful soup is used to convert the website to its html code
#selenium is used to control the website

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

from selenium.webdriver.chrome.service import Service
service=Service(executable_path="/Users/tuhina/Desktop/coding/C127/chromedriver")
options=webdriver.ChromeOptions()
browser=webdriver.Chrome(service=service, options=options)
browser.get(START_URL)

time.sleep(10)

scraped_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table = soup.find("table", attrs={"class", "wikitable"})

    table_body = bright_star_table.find('tbody')

    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all("td")
        print(table_cols)

        temp_list = []

        for col_data in table_cols:
	        #print(col_data.text)
            data = col_data.text.strip()
            print(data)
            temp_list.append(data)

        scraped_data.append(temp_list)

stars_data = []

for i in range(0, len(scraped_data)):
    star_names = scraped_data[i][1]			
    distance = scraped_data[i][3]
    mass = scraped_data[i][5]
    radius = scraped_data[i][6]			
    lum = scraped_data[i][7]
	
    required_data = [star_names, distance, mass, radius, lum]
    stars_data.append(required_data)

headers = ["star_names", "distance", "mass", "radius", "luminosity"]

star_df_1 = pd.DataFrame(stars_data, columns = headers)

star_df_1.to_csv("scraped_data.csv", index = True, index_label = "id")

###P128

page = requests.get(hyperlink)

soup = BeautifulSoup(browser.page_source, "html.parser")
tables = soup.find.all()

list = []

#step 3 dropping td
for td_tag in soup.find_all("td", attrs={"class"}):
    list = td_tag.find_all("td")

td_tag.drop('td',inplace = True)


list = pd.DataFrame(stars_data, columns=headers)

list.to_csv('updated_scraped_data.csv',index=True, index_label="id")


from os import link
import requests
from bs4 import BeautifulSoup
import json
url = "https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
sample_url = requests.get(url)
soup_data = BeautifulSoup(sample.text,"html.parser") 
def scrape_top_list():
    div=soup_data.find("div",class_="body_main container") 
    table=div.find("table",class_="table")
    tr=table.find_all('tr')
    details_list=[]
    for i in tr:
        tds=i.find_all('td')
        dic={}
        for j in tds:
            rank=i.find('td',class_='bold').get_text()[:-1]
            dic['rank']=rank
            rating=i.find('span',class_='tMeterScore').get_text()[1:]
            dic['rating']=rating
            movie_name=i.find('a',class_='unstyled articleLink')['href'][3:]
            dic['movie_name']=movie_name
            reviews=i.find('td',class_='right hidden-xs').get_text()
            dic['reviews']=reviews
            url=i.find('a',class_='unstyled articleLink')['href']
            link='https://www.rottentomatoes.com'+url
            dic["url"]=link
            year=i.find('a',class_="unstyled articleLink").get_text().strip()[-5:-1]
            dic["year"]=year
        if dic=={}:
            del dic 
        else:
            details_list.append(dic)
    with open("task1.json","w+") as file:
        json.dump(details_list,file,indent=4)
        return details_list
scrape_top_list()
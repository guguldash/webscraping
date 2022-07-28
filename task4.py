import requests
from bs4 import BeautifulSoup
import json
import pprint
def scrape_movie_details(url1):
    url = (url1)
    movie_page = requests.get(url)
    soup_data=BeautifulSoup(movie_page.text,'html.parser')
    dict={}
    one_div = soup_data.find('div',class_='container')
    body = one_div.find("div",class_="media-body")
    list= body.find_all("li") 
    movie_name=one_div.find("h1", slot="title").get_text()
    dict["movie_name"]=movie_name
    for vlu in list:
        data=vlu.text
        var=data.split()
        if 'Rating:' in var:
            dict['rating']=var[1]
        elif "Genre:" in var:
            dict['Genre']=var[1:]
        elif 'Language:' in var:
            dict['Language']=var[2:]
        elif 'Director:' in var:
            a=var[1:]
            d=" "
            for k in a:
                d+=k
            d=d.split(",")

            dict['Director']=d
        elif 'Runtime:' in var:
            run=var[1:]
            for run_vlu in range (len(run)):
                if "h" in run[run_vlu]:
                    hour=int(run[run_vlu][ :-1])*60
                elif "m" in run[run_vlu]:
                    min=int(run[run_vlu][ :-1])
            movie_time = hour+min 
            dict['Runtime'] = movie_time
        elif 'Distributor:' in var: 
            dict['Distributor']=var[2:]
    # with open("task4.json","w+") as file: 
    #     json.dump(dict,file,indent=4) 
            return (dict)
    # return(dict) 
# url1="https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse" 
# (scrape_movie_details(url1))
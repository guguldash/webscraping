import requests
from bs4 import BeautifulSoup
import json
url="https://www.rottentomatoes.com/m/toy_story_4"
def movie_actor_details(url):
    sample=requests.get(url)
    soup_data=BeautifulSoup(sample.text,"html.parser")

    div=soup_data.find("div",class_ = "castSection")
    div1=div.find_all("div",class_="cast-item media inlineBlock")
    div2=div.find_all("div",class_="cast-item media inlineBlock moreCasts hide")

    movie_data_list=[]
    for vlu in div1:
        a=vlu.find("a")["href"][11:]
        data_dic = {"actor_name": a}
        movie_data_list.append(data_dic)

    for vlu2 in div2:
        a1=vlu2.find("a")["href"][11:]
        data_dic1 = {"actor_name": a1}
        list.append(data_dic1)

    with open("task12.json","w+") as file:
        json.dump(list, file,indent=4)
        return movie_data_list

movie_actor_details(url)
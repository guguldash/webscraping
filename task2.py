import pprint
from task1 import scrape_top_list 
import json
movie_detail=scrape_top_list()
def group_by_year(all_movies):
    unic_year=[]
    for movie in all_movies:
        year=movie["year"]
        if year not in unic_year:
            unic_year.append(year)
            unic_year.sort()

    movie_dic={i:[] for i in unic_year}
    for mov in all_movies:
        year=mov["year"]
        for movi in movie_dic:
            if str(movi)==str(year):
                movie_dic[movi].append(movi)
    with open ("task2.json","w+") as file:
        json.dump(movie_dic,file,indent=4)
    return (movie_dic)
group_by_year(movie_detail)   
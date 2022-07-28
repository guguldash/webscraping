from task5 import*
import json
with open("task5.json","r") as file:
    movie_language=json.load(file)
def analyse_movies_directors():
    directors_dic={}
    for vlu in movie_language:
        if "Director" in vlu:
            for vlu2 in vlu["Director"]:
                if vlu2 in directors_dic:
                    directors_dic[vlu2]=directors_dic[vlu2]+1
                if vlu2 not in directors_dic:
                    directors_dic[vlu2]=1
    with open("task7.json","w+") as file:
        json.dump(directors_dic,file,indent=4)
analyse_movies_directors()
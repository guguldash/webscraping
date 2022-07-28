from task5 import*
import json
with open("task5.json","r") as file:
    movie_language=json.load(file)
def analyse_movies_directors():
    movies_language_dic={}
    for movie in movie_language:
        if "Language" in movie:
            for language in movie["Language"]:
                if language in movies_language_dic:
                    movies_language_dic[language]=movies_language_dic[language]+1
                if language not in movies_language_dic:
                    movies_language_dic[language]=1
    with open("task6.json","w+") as file:
        json.dump(movies_language_dic,file,indent=4)
analyse_movies_directors() 
import os
import random
import time
import json
with open("task5.json","r+") as movies_file:
    all_movies_data=json.load(movies_file)
def data_txt():
    time = random.randint(1,3)
    for movies in all_movies_data:
        path = "/home/admin123/Desktop/mytask9/mytask9999"+movies["movie_name"]+".json"
        if not os.path.exists(path):
            moviesdata_file= open(path,"w+")
            json.dump(movies,moviesdata_file,indent=4)
        time.sleep(time)
data_txt()
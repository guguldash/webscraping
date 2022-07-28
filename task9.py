import os
import random
import time
import json
movies_file = open("task5.json","r+")
all_movies_data=json.load(movies_file)
movies_file.close()
def data_txt():
    time = random.randint(1,3)
    for movies in all_movies_data:
        path = "/home/admin123/Desktop/mytask9/mytask9999"+movies["movie_name"]+".json"
        if os.path.exists(path):
            pass
        else:
            moviesdata_file= open(path,"w+")
            json.dump(movies,moviesdata_file,indent=4)
        time.sleep(time)
data_txt()
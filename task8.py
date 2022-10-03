import json
import requests 
import os 
with open("task1.json","r+") as file8:
    movies_data=json.load(file8) 
def txt(all_data):
    for movie in all_data: 
        path=("/home/admin123/Desktop/mycode/task8"+movie["movie_name"]+".text")
        if not os.path.exists(path):
            with open("/home/admin123/Desktop/mycode/task8"+movie["movie_name"]+".text","w") as create:
                url=requests.get(movie["url"])
                create1=create.write(url.text)
txt(movies_data)  
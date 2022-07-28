import json
data_file=open("task5.json" , "r")
data=json.loads(data_file.read())
data_dic={}
def get_genre_details():
    for vlu in data:        
        if "Genre" in vlu:
            var=vlu["Genre"]
            for vlu2 in var:
                if vlu2 in data_dic:
                    data_dic[vlu2]+=1
                else:
                    data_dic[vlu2] = 1
    with open("task11.json","w+") as file:
        json.dump(data_dic, file, indent = 4)
get_genre_details()
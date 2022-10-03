import json

data_file=open("task5.json","r")
data=json.loads(data_file.read())

def movie_direc_lang(movies):
    list=[]
    data_dict={}
    for vlu in movies:
        direc = vlu["Director"]
        for vlu1 in direc:
            if vlu1 not in list:
                list.append(j)
    # dict={}
    for vlu2 in list:
        dic={}
        for vlu3 in vlu2:
            
            if vlu3 in vlu3["Director"] and "Languagre" in vlu3:
                for language in vlu3['Languagre']:
                    if language in dic:
                        dic[language]=dic[language]+1
                    if language not in dic:
                        dic[language]=1
        data_dict[vlu3]=dic

        with open("task10.json","w+") as file:
            json.dump(data_dict,file, indent=4)
movie_direc_lang(data)

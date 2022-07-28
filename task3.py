from task1 import scrape_top_list
details=scrape_top_list()
def group_by_decade(movies):
    unique_year=[] 
    movie_dic={} 
    for value in movies:
        for year in value:
            if year=="year":
                if (value[year]) not in unique_year:
                    unique_year.append(value[year])
        unique_year.sort() 
    decate_movie_list=[] 
    for vlu1 in unique_year:
        mod=int(vlu1)%10 
        decode=int(vlu1)-mod 
        if decode not in decate_movie_list: 
            decate_movie_list.append(decode)
    for vlu2 in decate_movie_list:
        movie_dic[vlu2]=[]

    for vlu3 in movie_dic:
        dec10=int(vlu3)+9
        for movie in movies:
            for yr in movie:
                if yr =="year":
                    if (int(movie[yr]))<=dec10 and (int(movie[yr]))>=vlu3:
                        movie_dic[vlu3].append(movie)
    import json
    with open("task3.json","w+") as file: 
        json.dump(movie_dic,file,indent=4) 
    return(movie_dic) 
group_by_decade(details)
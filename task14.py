from task1 import top_movies
from task4 import scrape_movie_details
from task12 import scrap_movie_cast
from pprint import pprint

def analyse_co_actors(top_movies):
	main_dic={}
	for x in top_movies:
		url=x["url"]
		a=scrap_movie_cast(url)
		main_actor_id=a[0]["imdb_id"]
		main_actor_name=a[0]["name"]
		n=0
		for i in a[0:6]:
			if n==0:
				if i["imdb_id"] not in main_dic:
					main_dic[main_actor_id]={}
					main_dic[main_actor_id]["name"]=main_actor_name
					main_dic[main_actor_id]["frequent_co_actors"]=[]
				n+=1
			else:
				flag=True
				for j in main_dic[main_actor_id]["frequent_co_actors"]:
					if j["imdb_id"]==i["imdb_id"]:
						j["num_movie"]+=1
						flag=False
				if flag:
					new_dic={}
					new_dic["name"]=i["name"]
					new_dic["imdb_id"]=i["imdb_id"]
					new_dic["num_movie"]=1
				main_dic[main_actor_id]["frequent_co_actors"].append(new_dic)
	return main_dic

# pprint(analyse_co_actors(top_movies))
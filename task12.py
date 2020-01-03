import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint
from os import path
from task1 import top_movies
def scrap_movie_cast(movie_url):
	filename=movie_url[27:36]+"_cast.json"
	if path.exists(filename):
		with open(filename,"r") as file:
			data=json.load(file)
			return data
	else:
		data=requests.get(movie_url).text
		soup=BeautifulSoup(data,"html.parser")
		main_div=soup.find("div",class_="article listo")
		table=main_div.find("table",class_="cast_list")
		trs=table.find_all("tr")
		cast_list=[]
		for tr in trs:
			dic={}
			actor=tr.find("td",class_="")
			if actor != None:
				imdb_id=actor.find("a").get("href")[6:15]
				name=actor.find("a").text.strip()
				dic["imdb_id"]=imdb_id
				dic["name"]=name
				cast_list.append(dic)
		with open (filename,"w") as file:
			json.dump(cast_list,file)
		with open(filename,"r") as file:
			data=json.load(file)
			return data
		
# for i in top_movies:
# 	url=i["url"]+"fullcredits?ref_=tt_cl_sm#cast"
	# pprint(scrap_movie_cast(url))
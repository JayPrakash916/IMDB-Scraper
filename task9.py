# web scraping task9 #### 

import random,time
from task4 import scrape_movie_details
from os import path
import json 
from pprint import pprint
from task1 import top_movies
import requests
from bs4 import BeautifulSoup
def scrape_movie_json(s):
	all_data=[]
	for i in s:
		u=i["url"]
		filename=u[27:36]+".json"
		if path.exists(filename):
			with open(filename,"r") as file:
				data=json.load(file)
				all_data.append(data)


		else:
			second=random.randint(1,3)
			time.sleep(second)
			movie_data=scrape_movie_details(u)
			with open(filename,"w") as file:
				json.dump(movie_data,file)
				
			with open(filename,"r") as file:
				data=json.load(file)
				all_data.append(data)
	return all_data

movie_list=scrape_movie_json(top_movies)
# pprint(movie_list)

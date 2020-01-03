# web scraping task 8 ######

from task4 import scrape_movie_details
from os import path
import json 
from pprint import pprint
from task1 import top_movies
import requests
from bs4 import BeautifulSoup
def scrape_movie_json(s):
	all_movie=[]
	for i in s:
		u=i["url"]
		filename=u[27:36]+".json"
		if path.exists(filename):
			with open(filename,"r") as file:
				data=json.load(file)
				# pprint (data)
				all_movie.append(data)

		else:
			movie_data=scrape_movie_details(u)
			with open(filename,"w") as file:
				json.dump(movie_data,file)
				# pprint (movie_data)
			with open(filename,"r") as file:
				data=json.load(file)
				# pprint (data)
				all_movie.append(data)
	return all_movie
	         



all_movie=scrape_movie_json(top_movies)
# pprint(all_movie)



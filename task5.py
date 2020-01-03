# web scraping task5 
import json
from pprint import pprint
from task1 import top_movies
from task4 import scrape_movie_details

def get_movie_list_details(movie_list):
	details=[]
	for i in movie_list:
		url=i["url"]
		a=scrape_movie_details(url)
		details.append(a)

	return details

movie_details=(get_movie_list_details(top_movies[:10]))
# pprint(movie_details)

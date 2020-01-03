# web scraping ka dusara task2
import json
from pprint import pprint

with open("all_movie.json","r")as war:
	movies=json.load(war)
	# print(movies)

	
def gruop_by_year(movies):
	dict_year={}
	for i in movies:
		a=i["Year"]	
		if a not in dict_year:
			dict_year[a]=[]
			dict_year[a].append(i)
		else:
			dict_year[a].append(i)

	return dict_year

# data=(gruop_by_year(movies))
# pprint(data)


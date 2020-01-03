from task5 import movie_details
from pprint import pprint

def analyse_movies_directors(movie_details):
	director_list={}
	for movie in movie_details:
		for director in movie["director"]:
			if director in director_list:
				director_list[director]+=1
			else:
				director_list[director]=1
	return director_list


# pprint(analyse_movies_directors(movie_details))
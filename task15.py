from task1 import top_movies
from task13 import movie_cast_movie_details
from pprint import pprint


movie_list = []
for i in top_movies:
	url = i['url']
	data = movie_cast_movie_details(url)
	movie_list.append(data)



def analyse_actors(movie_list):
	actors = {}
	for data in movie_list:
		for i in data['cast']:
			if i['imdb_id'] not in actors:
				actors[i['imdb_id']]={}
				actors[i['imdb_id']]['name'] = i['name']
				actors[i['imdb_id']]['num_movie'] = 1
			else:
				actors[i['imdb_id']]['num_movie'] +=1
	return actors

pprint(analyse_actors(movie_list))



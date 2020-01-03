from task9 import movie_list
from pprint import pprint


def analysis_movies_genre(movie_list):
	dict2={}
	for i in movie_list:
		for genre in i["genre"]:
			if genre not in dict2:
				dict2[genre]=1
			else:
				 dict2[genre]+=1
	return dict2


# pprint(analysis_movies_genre(movie_list))
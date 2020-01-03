from task5 import movie_details
from pprint import pprint


def analyse_movies_language(movie_details):
	language={}
	for i in movie_details:
		for j in i["language"]:
			
			if j in language:
				language[j]+=1
			else:
				language[j]=1
	return(language)


# pprint(analyse_movies_language(movie_details))
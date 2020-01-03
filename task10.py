from  task9 import movie_list
from pprint import pprint



def analysis_language_and_directors(movies_list): 
	dic={}
	for movie in movies_list:
		for dire in movie["director"]:
			if dire not in dic:
				dic[dire]={}
				for lan in movie["language"]:
					if lan not in dic[dire]:
						dic[dire][lan]=1
					else:
						dic[dire][lan]+=1
			else:
				for lan in movie["language"]:
					if lan not in dic[dire]:
						dic[dire][lan]=1
					else:
						dic[dire][lan]+=1
	return dic


# a=analysis_language_and_directors(movie_list)
# pprint(a)


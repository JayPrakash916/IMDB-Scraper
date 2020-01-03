from task1 import top_movies
from task4 import scrape_movie_details
from task12 import scrap_movie_cast
from pprint import pprint

	
def movie_cast_movie_details(link):
	url=link+"fullcredits?ref_=tt_cl_sm#cast"
	movie_details=scrape_movie_details(link)
	cast=scrap_movie_cast(url)
	movie_details["cast"]=cast
	return movie_details


		
# for i in top_movies:
# 	link=i["url"]
# 	a=movie_cast_movie_details(link)
# 	pprint(a)


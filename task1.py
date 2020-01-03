# web scraping ka pahla task do tarike se kiya hu

# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint

# url="https://www.imdb.com/india/top-rated-indian-movies/"
# page=requests.get(url)

# soup=BeautifulSoup(page.text,'html.parser')


# movie_list=[]
# def scrap_top_list():
# 	main_div=soup.find('div',class_='lister')
# 	tbody=main_div.find('tbody',class_='lister-list')
# 	trs=tbody.find_all('tr')
	

# 	movie_position=[]
# 	movie_name=[]
# 	year_movie=[]
# 	rating_movie=[]
# 	url_movie=[]
# 	for tr in trs:
# 		dic={}
# 		position=tr.find('td',class_='titleColumn').get_text().strip()
# 		rank=''
# 		for i in position:
# 			if '.' not in i:
# 				rank=rank+i
# 			else:
# 				break
# 		movie_position.append(rank)

# 		tital=tr.find('td',class_='titleColumn').a.get_text()
# 		movie_name.append(tital)

# 		year=tr.find('td',class_='titleColumn').span.get_text().strip('()')
# 		year_movie.append(year)

# 		rate=tr.find('td',class_='ratingColumn imdbRating').strong.get_text()
# 		rating_movie.append(rate)

# 		link=tr.find('td',class_='titleColumn').a['href']
# 		url="https://www.imdb.com"+link
# 		url_movie.append(url)

# 		dic["name"]=tital
# 		dic["year"]=int(year)
# 		dic["position"]=int(rank)
# 		dic["rating"]=float(rate)
# 		dic["url"]=url
		
# 		movie_list.append(dic)
# 	return movie_list

# pprint(scrap_top_list())

####################dusra tarika########################



import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint
from os import path

def scrap_top_list():
	if path.exists("all_movie.json"):
		with open("all_movie.json") as file:
			movie_list=json.load(file)
	else:
		movie_list=[]
		big_dict = {}
		url="https://www.imdb.com/india/top-rated-indian-movies/"
		page=requests.get(url)
		soup=BeautifulSoup(page.text,'html.parser')
		main_div=soup.find('div',class_='lister')
		tbody=main_div.find('tbody',class_='lister-list')
		trs=tbody.find_all('tr')
		for tr in trs:
			dic={}
			position=tr.find('td',class_='titleColumn').get_text().strip()
			rank=''
			for i in position:
				if '.' not in i:
					rank=rank+i
				else:
					break

			dic["position"]=int(rank)

			tital=tr.find('td',class_='titleColumn').a.get_text()
			dic["Name"]=tital

			year=tr.find('td',class_='titleColumn').span.get_text().strip('()')
			dic["Year"]=int(year)

			rate=tr.find('td',class_='ratingColumn imdbRating').strong.get_text()
			dic["rating"]=float(rate)

			link=tr.find('td',class_='titleColumn').a['href']
			url="https://www.imdb.com"+link
			dic["url"]=url
			movie_list.append(dic)

		with open("all_movie.json","w")as file:
			json.dump(movie_list,file)
		
	return movie_list


top_movies=(scrap_top_list())
# pprint(top_movies)






		


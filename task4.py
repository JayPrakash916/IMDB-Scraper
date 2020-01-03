# web scraping ka task4
from pprint import pprint 
import requests
from bs4 import BeautifulSoup


def scrape_movie_details(movie_url):
	page=requests.get(movie_url)
	soup=BeautifulSoup(page.text,'html.parser')

	dict1={}
	# here i find movie name
	name_div=soup.find("div",class_="title_wrapper").h1.text
	movie_name=""
	for i in name_div:
		if i in "(":
			break
		else:
			movie_name+=i

	# here i find dicrector name and put it in Directro list 
	Director=[]
	director_div=soup.find("div",class_="credit_summary_item")
	director=director_div.find_all("a")
	for i in director:
		name=i.text
		Director.append(name)
	
	# here i find genere
	genre=[]
	gener_div=soup.find("div",class_="subtext").find_all("a")
	gener_div.pop()
	for i in gener_div:
		a=i.text
		genre.append(a)

	# here i find bio of movie
	bio_div=soup.find("div",class_="summary_text")
	bio=bio_div.text.strip()

	# here i find poster url
	poster_div=soup.find("div",class_="poster").a.get("href")
	poster="https://www.imdb.com"+poster_div

	# here i find country and language and runtime
	county_lang_div=soup.find("div",attrs={"class":"article","id":"titleDetails"})
	country_div=county_lang_div.find_all(class_="txt-block")
	language=[]
	new_time=''
	for i in country_div:
		try:
			a=(i.find("h4")).text
			# for country
			if a=="Country:":
				country=(i.a.text)

			# for language	
			elif "Language:" in a:
				language_div=(i.find_all("a"))
				for j in language_div:
					language.append(j.text)

			# for runtime		
			elif a=="Runtime:":
				time=(i.time.text)
				for k in time:
					if k in "minhr ":
						pass
					else:
						new_time+=k
		except AttributeError:
			continue

	# here i put all the data in my final dictonery 
	dict1["name"]=movie_name.strip()
	dict1["director"]=Director
	dict1["country"]=country
	dict1["language"]=language
	dict1["poster_image_url"]=poster
	dict1["bio"]=bio
	dict1["runtime"]=new_time
	dict1["genre"]=genre

	return dict1


url="https://www.imdb.com/title/tt0986264/"
# movie_details=(scrape_movie_details(url))
# pprint(movie_details)
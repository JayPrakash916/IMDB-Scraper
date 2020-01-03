# web scraping ka tisra task3

from task2 import movies
from pprint import pprint

def group_by_decade(movies):
	dic={}
	for i in movies:
		year=i["Year"]
		decade=''
		a=0
		for j in str(year):
			if a==3:
				j=0
				decade+=str(j)
			else:
				decade+=j
				a+=1
				
		decade=int(decade)
		if decade not in dic:
			dic[decade]=[]
			dic[decade].append(i)
		else:
			dic[decade].append(i)
	return dic


# pprint(group_by_decade(movies))
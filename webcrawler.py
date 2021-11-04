import requests
from bs4 import BeautifulSoup


user_input = input("What you want ?! : ")

payload = {"query" : str(user_input) , "available" : "true" , "sort" : "-price"}

respons = requests.get("https://www.torob.com/search/" , payload)

soup = BeautifulSoup(respons.content , 'lxml')

for item in soup.find_all("a" ,{"class" : "jsx-2021336621"}):
	print(item.get_text())
print(respons.url)
import requests
from bs4 import BeautifulSoup
import csv

def get_gsearch_results(q):
	q += " LinkedIn Northrop Grumman"
	q.replace(" ", "%20");
	print("searching " + q)
	page = requests.get("https://www.google.com/search?q=" + q)
	soup = BeautifulSoup(page.content)
	import re
	pattern = re.compile("https://www.linkedin.com/in/*")

	link_list = []
	for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
	    link = re.split(":(?=http)",link["href"].replace("/url?q=",""))[0]
	    ind = link.find('&sa')
	    if(ind != -1):
	    	link = link[0:ind]
	    if pattern.match(link):
	    	link_list.append(link)

	return link_list

# linkedin names available during company search
file = open('C:\\Users\\ryanw\\Desktop\\ng_linkedins.txt', 'r')
lines = file.readlines()
link_set = set()
for line in lines:
	link_set.add(line)

# result csv from https://phantombuster.com/automations/linkedin/3112/linkedin-profile-scraper
with open('C:\\Users\\ryanw\\Downloads\\result.csv', newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for link in get_gsearch_results(row['job']):
        	link_set.add(link)

big_file = open('C:\\Users\\ryanw\\Desktop\\ng_linkedins_large_v2.txt', 'w+')
for link in link_set:
	big_file.write(link + "\n")

file.close()
big_file.close()
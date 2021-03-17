import requests
from os import listdir
from os.path import isfile, join
import csv
files = [f for f in listdir('./data') if isfile(join('./data', f))]
print(files)
token_file = open('./bitly_access_tok', 'r')
token = token_file.read().replace('\n', '')

headers={"Authorization":"Bearer " + token}
# res = requests.get(url="https://api-ssl.bitly.com/v4/groups", headers=headers)
# print(res)
# print(res.json())

linksDict = dict()
with open('./linkmapping.csv', newline='', encoding="utf-8", mode='r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
    	linksDict[row[0]] = row[1]


for link in linksDict.keys():
	#index = linksDict[link].find("https://bitly.is/") + len("https://bitly.is/")
	index = linksDict[link].find("https://") + len("https://")

	bitLink = linksDict[link][index:]
	print(bitLink)
	url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitLink}/clicks/summary"
	print(url)
	result = requests.get(url=url, headers=headers)
	print(result)
	print(result.text)
	# result = requests.post(url="https://api-ssl.bitly.com/v4/shorten", json=data, headers=headers).json()
	# print(result)
	# newLink = result['link']
	# linkTuples.append((file, newLink))

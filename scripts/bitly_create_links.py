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

linkTuples = []
for file in files:
	long_link = "https://dev.bitly.com"
	data = { "group_guid": "Bl3a07x9BrH", "domain": "bit.ly", "long_url": long_link }
	result = requests.post(url="https://api-ssl.bitly.com/v4/bitlinks", json=data, headers=headers).json()
	print(result)
	newLink = result['link']
	linkTuples.append((file, newLink))

with open('./linkmapping.csv', newline='', encoding="utf-8", mode='w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for group in linkTuples:
    	writer.writerow([group[0], group[1]])

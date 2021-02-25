import json
import os

def read_and_rename(filename):
	# Open a file: file
	file = open(filename,mode='r', encoding="utf8")
	 
	# read all lines at once
	obj = json.loads(file.read())
	new_name = obj['profile']['name']
	# close the file
	file.close()

	return new_name.replace(" ", "_").replace("\"", "")

folder_dir = "C:\\Users\\ryanw\\Desktop\\linkedins"
for f in enumerate(os.listdir(folder_dir)):
	filename = f[1]
	dst = read_and_rename(folder_dir + "\\" + filename)
	os.rename(folder_dir + "\\" + filename, "C:\\Users\\ryanw\\Desktop\\linkedin_names\\" + dst + ".txt")
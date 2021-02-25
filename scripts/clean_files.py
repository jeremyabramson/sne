file = open('C:\\Users\\ryanw\\Desktop\\ng_linkedins_large.txt', 'r')
lines = file.readlines()
link_set = set()
for line in lines:
	if len(line) != 0:
		link_set.add(line)

big_file = open('C:\\Users\\ryanw\\Desktop\\ng_linkedins_large_clean.txt', 'w+')
for link in link_set:
	ind = link.find('%3Ftrk')
	if(ind != -1):
		link = link[0:ind]

	ind2 = link.find('/%257')
	if(ind2 != -1):
		link = link[0:ind2]
	big_file.write(link + "\n")
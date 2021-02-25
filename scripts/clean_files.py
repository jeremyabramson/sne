file = open('C:\\Users\\ryanw\\Desktop\\ng_linkedins_large_v2.txt', 'r')
lines = file.readlines()
link_set = set()
for line in lines:
	if len(line) != 0:
		link_set.add(line)

big_file = open('C:\\Users\\ryanw\\Desktop\\ng_linkedins_large_v2_clean.txt', 'w+')
for link in link_set:
	big_file.write(link)
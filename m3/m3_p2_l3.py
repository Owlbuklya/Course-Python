d = {'name1':'id1', 'name2':'id2', 'name3':'id3'}

for key, value in d.items():
	d.pop(key)
	d[value] = key

print(d)
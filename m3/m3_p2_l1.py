l = [1, 4, 1, 6, 'hello', 'a', 5, 'hello', 1] 
m = []
j = 1

for item in l:
	for i in range(j,len(l)):
		if item == l[i]:
			if item not in m:
				m.append(item)
			else:
				continue
	j += 1
	
print(m)
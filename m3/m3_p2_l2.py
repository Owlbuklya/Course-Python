from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]

m_sort = []

for item in m:
	print(item)
	m_sort.append(sorted(item)[n-1])

print(f'Максимальный элемент равен {sorted(m_sort)[n-1]}')

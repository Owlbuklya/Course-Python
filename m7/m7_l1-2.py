import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

url = 'http://mfd.ru/currency/?currency=USD'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

pars_data = soup.find('table', class_ = 'mfd-table mfd-currency-table').find_all('td')

data = (i.text for i in pars_data)

data_list = []

for i in data:
	data_list += str(i).split()

data_list[2] = data_list[2].replace('*','')

dates = [] # ось x
rates = [] # ось y	

for i in range(len(data_list)-2, 0, -4):
	rates.append(float(data_list[i]))
	dates.append(data_list[i-1])


f, ax = plt.subplots()
f.set_size_inches(7, 4)    
f.set_facecolor('#eee')
ax.plot(dates, rates)
ax.grid(True)
ax.set_xlabel('Даты') 
ax.set_ylabel('Курс')
ax.set_title('График изменения курса доллара к рублю ')
ax.xaxis.set_major_locator(MaxNLocator(5))
plt.show()
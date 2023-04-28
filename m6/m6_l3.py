import requests
from threading import Thread
import time

def get_html(link):
	response = requests.get(link)
	return response.text

list_link = ['https://brunoyam.com', 'https://github.com', 'https://www.python.org', 'https://ya.ru/', 'https://www.google.ru']

t1 = time.time()
for url in list_link:
	get_html(url)
operating_time_1 = time.time() - t1

print(f"Время работы последовательного запуска потоков - {operating_time_1} сек.")

t2 = time.time()
threads = [Thread(target = get_html, args = (url, )) for url in list_link]

for t in threads:
	t.start()

for t in threads:
	t.join()
operating_time_2 = time.time() - t2

print(f"Время работы параллельного запуска потоков - {operating_time_2} сек.")
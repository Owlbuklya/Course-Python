import time
from threading import Thread


def get_thread(thread_name):
	print(f'{thread_name}')
	time.sleep(1)

t1 = time.time()

print('\n<<<Последовательный запуск>>>')
for i in range(5):
	name = (f'Поток {i + 1}')
	get_thread(name)

operating_time_1 = time.time() - t1

t2 = time.time()

print('\n<<<Параллельный запуск>>>')
threads = [Thread(target = get_thread, args=(f'Поток {i + 1}', )) for i in range(5)]

for t in threads:
	t.start()

for t in threads:
	t.join()

operating_time_2 = time.time() - t2


print(f"""Время работы последовательного запуска потоков - {operating_time_1} сек.
Время работы параллельного запуска потоков - {operating_time_2} сек.""")
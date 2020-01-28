from concurrent.futures import ThreadPoolExecutor
import time

def wait():
	time.sleep(1)
	print("Waiting...")

start = time.perf_counter()

for i in range(6):
	wait()

end = time.perf_counter()

total = round(end - start, 2)

print(total)
from concurrent.futures import ThreadPoolExecutor
import time

def wait(n):
	time.sleep(1)
	return f"Waiting...{n}"

start = time.perf_counter()

with ThreadPoolExecutor() as executor:
	results = executor.map(wait, range(1,10))

for r in results:
	print(r)

end = time.perf_counter()

total = round(end - start, 2)

print(total)
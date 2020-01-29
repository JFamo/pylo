from concurrent.futures import ThreadPoolExecutor
import time

def wait(n):
	time.sleep(1)
	print(f"Waiting...{n}")

start = time.perf_counter()

with ThreadPoolExecutor() as executor:
	executor.map(wait, range(1,7))

end = time.perf_counter()

total = round(end - start, 2)

print(total)
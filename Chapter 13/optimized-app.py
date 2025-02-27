1.	Optimized Python code:
2.	
3.	import time
4.	import random
5.	
6.	def optimized_cpu_task():
7.	start = time.time()
8.	while time.time() - start < 2:
9.	x = sorted(random.random() for _ in range(10000))
10.	
11.	if __name__ == "__main__":
12.	while True:
13.	optimized_cpu_task()
14.	time.sleep(1)


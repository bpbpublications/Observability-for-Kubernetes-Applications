1.	import time
2.	import random
3.	
4.	def cpu_int_task():
5.	start = time.time()
6.	while time.time() - start < 2:
7.	x = [random.random() for _ in range(10000)]
8.	x.sort()
9.	
10.	if __name__ == "__main__":
11.	while True:
12.	cpu_int_task()
13.	time.sleep(1)


import threading
import multiprocessing

def worker(num):
    print(f"Worker {num} started")
    for i in range(5):
        print(f"Worker {num}: {i}")
    print(f"Worker {num} finished")

# Multithreading example
threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Multiprocessing example
processes = []
for i in range(3):
    p = multiprocessing.Process(target=worker, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

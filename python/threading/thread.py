import threading

def worker():
    print('Worker'+threading.current_thread().name)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker ,name=str(i))
    threads.append(t)
    t.start()
    
# Wait for all threads to complete
for t in threads:
    t.join()
    
print("main thread")
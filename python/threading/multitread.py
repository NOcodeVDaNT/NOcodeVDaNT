import threading

def print_numbers():
    for i in range(3):
        print(f"{threading.current_thread().name}: {i}")

# Creating multiple threads
t1 = threading.Thread(target=print_numbers, name="Thread-1")
t2 = threading.Thread(target=print_numbers, name="Thread-2")

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads finished execution!")

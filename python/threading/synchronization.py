import threading
import time

balance = 0
lock = threading.Lock()  # Creating a Lock

def deposit(amount):
    global balance
    with lock:  # Ensures only one thread modifies balance at a time
        local_balance = balance
        time.sleep(0.1)
        local_balance += amount
        balance = local_balance
        print(f"Deposited {amount}, Balance: {balance}")

t1 = threading.Thread(target=deposit, args=(100,))
t2 = threading.Thread(target=deposit, args=(200,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Final Balance: {balance}")  # Correct balance: 300

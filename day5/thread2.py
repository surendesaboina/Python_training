
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()  # Start the thread
thread.join()   # Wait for the thread to finish

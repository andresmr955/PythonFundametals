

import threading
import time

print_lock = threading.Lock()  # Crear un lock global
#function to simulate a time-consuming task

def process_request(request_id):
    with print_lock:
        print(f"Processing request {request_id}")
        time.sleep(2) # Simulate a time-consuming task
    with print_lock:
        print(f"Request {request_id} Completed")

threads = []
for i in range(3):
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()
#wait for all threads to complete

for thread in threads:
    #Assure that the thread has completed before moving on
    thread.join()

print("All requests have been processed.")

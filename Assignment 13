import threading
import time


# Task 1: Print numbers
def print_numbers():
    for i in range(1, 6):
        print(f"Thread 1 - Number: {i}")
        time.sleep(1)


# Task 2: Print alphabets
def print_alphabets():
    for char in "ABCDE":
        print(f"Thread 2 - Alphabet: {char}")
        time.sleep(1)


# Task 3: Calculate squares
def calculate_squares():
    for i in range(1, 6):
        print(f"Thread 3 - Square of {i}: {i ** 2}")
        time.sleep(1)


# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_alphabets)
t3 = threading.Thread(target=calculate_squares)

# Start threads
print("Starting all threads...\n")

t1.start()
t2.start()
t3.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()

print("\nAll threads have completed their tasks.")

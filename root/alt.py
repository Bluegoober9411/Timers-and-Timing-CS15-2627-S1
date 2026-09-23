import time

start_time = time.monotonic()

timer_length = 2

while True:
    current_time = time.monotonic()
    elapsed_time = current_time - start_time
    if elapsed_time > timer_length:
        print("its been 2 seconds")
        start_time = time.monotonic()
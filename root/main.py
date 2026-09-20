import time
import random

reaction_times = []

print("Reaction Time Game!")
print("When you see GO!, press Enter as quickly as possible.")
print()

for attempt in range(1, 6):
    print(f"Attempt {attempt}/5")
    print("Get ready...")

    # Wait a random time between 2 and 5 seconds
    wait_time = random.uniform(2, 5)
    time.sleep(wait_time)

    # Record start time when GO! appears
    print("GO!")
    start_time = time.monotonic()

    # Wait for player response
    input()

    # Record end time when Enter is pressed
    end_time = time.monotonic()

    # Calculate reaction time
    reaction_time = end_time - start_time
    reaction_times.append(reaction_time)

    print(f"Reaction Time: {reaction_time:.3f} seconds\n")

# Find and display fastest reaction time
fastest_time = min(reaction_times)

print("Game Over!")
print(f"Fastest Reaction Time: {fastest_time:.3f} seconds")
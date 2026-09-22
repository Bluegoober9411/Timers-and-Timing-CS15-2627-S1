import time
import random
reaction_times = []
print("This game uses time as a factor. it is similar to ones you would find online."
      "the word NOW is going to appear, and you have to press enter as soon as possible.")
print()
for attempt in range(1, 10):
    print(f"Try {attempt}/10")
    print("Not yet")
    wait_time = random.uniform(1, 10)
    time.sleep(wait_time)
    print("NOW")
    start_time = time.monotonic()
    input()
    end_time = time.monotonic()
    reaction_time = end_time - start_time
    reaction_times.append(reaction_time)
    print(f"your speed was: {reaction_time:.3f} seconds\n")
fastest_time = min(reaction_times)
if fastest_time > 1 and fastest_time < 4:
    print("good job!")
if fastest_time > 4:
    print("did you go afk the whole time?")
if fastest_time > 1:
    print("cheater!!!")
print("Congrats! the game is finished")
print(f"Your fastest speed is: {fastest_time:.3f} seconds")
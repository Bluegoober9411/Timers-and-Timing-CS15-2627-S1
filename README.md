# Activity 7: Timers and Timing

In this activity, we will walk through how to use timing functions in Python to create delayed effects.

When you have completed the guided part of this activity, be sure to also complete the [Extension Activity](#extension-activity-reaction-time-game)!

## Overview of Using `time` in Python

Previously we learned how to use `time.sleep()` to pause a program for a specific number of seconds. It can be very useful tp pause a program, but the issue is that `time.sleep()` is a blocking function.

| Blocking                                                                                                         |
|:-----------------------------------------------------------------------------------------------------------------|
| *The program temporarily stops executing its current thread to wait for a timer, user input, or a system event.* |

This means that no other code of any kind can run during `time.sleep()`. While that may not seem like a very big deal right now, it can cause problems in more complex programs that require specific timing. Instead, we can build our own timer!

## 1. Create a Root Folder

Whenever you are creating a new Python project, it is best to stay organized by placing all the files related to the project in the same folder. Create a `root` folder.

Inside the folder, create a new `main.py` file.

## 2. `time.monotonic()` to Get a Time

Before we can start a timer, we need to know what time it is. Python has a special function:

```python
time.monotonic()
```

This function returns a value in seconds. The time in seconds is **not** relative to when the program starts running, but uses an internal clock on the device and is different from operating system to operating system. For Windows 11, it is the number of seconds since the computer was turned on. 

This relative time is useful, because we can define a time to start and a time to end. Even though `time.monotonic()` returns a value greater than 0, we can build or program to treat it as a relative starting time. 

## 3. Parts of a Timer

To build a timer, we need to be familiar with the values that a timer uses. In our example, we will create the following variables to act as parts of a timer:

* An iteration control structure that allows us to continuously check our timer.
* `start_time`: The time to start counting from.
* `current_time`: A value that continues to get updated with the current time every iteration of the loop.
* `timer_length`: A value in seconds for how long we want our timer to run for.
* `elapsed_time`: A value that represents the number of seconds passed since our `start_time`. We can calculate this with `current_time` - `start_time`.

## 4. Building the Timer

For this first example, we will build a simple timer that prints "Hello" once per second, without blocking the program.

```python
import time

# Set start_time to the current time
start_time = time.monotonic()

# Define how long the timer should run for
timer_length = 1

while True:
    # Update the current_time
    current_time = time.monotonic()
    
    # Calculate the elapsed_time from the difference between current_time and start_time
    elapsed_time = current_time - start_time
    
    # Compare elapsed_time to timer_length
    if elapsed_time >= timer_length:
        print("Timer complete!")
        print("Hello")
```

If you copy and paste this program as is, what happens? Does it successfully print "Hello" once per second? You might notice that it works once, and then immediately breaks.

This is because once the `elapsed_time` exceeds the `timer_length`, every loop after that `elapsed_time >= timer_length` evaluates to `True`!

We can fix this by starting our timer over by restarting our `start_time`.

```python
import time

# Set start_time to the current time
start_time = time.monotonic()

# Define how long the timer should run for
timer_length = 1

while True:
    # Update the current_time
    current_time = time.monotonic()
    
    # Calculate the elapsed_time from the difference between current_time and start_time
    elapsed_time = current_time - start_time
    
    # Compare elapsed_time to timer_length
    if elapsed_time >= timer_length:
        print("Timer complete!")
        print("Hello")

        # Restart timer
        start_time = time.monotonic()
```

Run the program again and see if it works!

# Extension Activity: Reaction Time Game

Create a reaction time game that uses `time.monotonic()` to measure how quickly the player responds to a prompt.

### Requirements

* Have the program wait for a **random amount of time between 2 and 5 seconds** before displaying `"GO!"`.
* Use `time.monotonic()` to record the time when `"GO!"` appears and again when the player presses Enter.
* Calculate and display the player's **reaction time in seconds**.
* Allow the player to complete **5 attempts** and display their reaction time after each attempt.
* After all 5 attempts, display the player's **fastest reaction time**.

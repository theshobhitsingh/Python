import time

# Configuration
initial_wait_time = 1     # Initial wait time in seconds
max_retries = 5           # Maximum number of retry attempts

# Initialization
wait_time = initial_wait_time
attempts = 0

print("Starting retry process...\n")

while attempts < max_retries:
    print(
        f"Attempt {attempts + 1} of {max_retries} | Waiting for {wait_time} seconds before next attempt...")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1

print("\nRetry process completed.")
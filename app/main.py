import time

def main():
    print("Welcome to Progresar!")
    print("Running for 5 minutes...")
    
    start_time = time.time()
    end_time = start_time + 300  # 300 seconds = 5 minutes
    
    while time.time() < end_time:
        # Simulate some work
        time.sleep(10)
        elapsed_time = int(time.time() - start_time)
        print(f"Running... Elapsed time: {elapsed_time} seconds")
    
    print("Progresar finished running after 5 minutes.")

if __name__ == "__main__":
    main()

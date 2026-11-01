import threading
import time


def process_data(name, delay):
    print(f"[{name}] Starting task...")
    time.sleep(delay)
    print(f"[{name}] Finished task!")


if __name__ == "__main__":
    print("--- Multithreading Demo ---")
    start_time = time.time()

    t1 = threading.Thread(target=process_data, args=("Worker-1", 2))
    t2 = threading.Thread(target=process_data, args=("Worker-2", 1.5))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"All threads completed in {time.time() - start_time:.2f} seconds.")
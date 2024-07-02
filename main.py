import time
import signal

running = True

def signal_handler(sig, frame):
    global running
    print("Stop signal received. Shutting down...")
    running = False

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def main():
    print("Memefreak starting up...")
    try:
        while running:
            print("Memefreak is running")
            time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        print("Memefreak shutting down...")

if __name__ == "__main__":
    main()
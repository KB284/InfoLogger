from pynput import keyboard

# Dictionary to store the count of each key press
key_count = {}

def on_press(key):
    try:
        # Increment the count for the pressed key
        key_count[key] = key_count.get(key, 0) + 1
        print(f"{key}")
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.end:
        # Stop listener on pressing the 'end' key
        return False

# Create a listener for keyboard events
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Start the listener
keyboard_listener.start()

# Wait for the listener to finish
keyboard_listener.join()
from pynput import keyboard, mouse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Dictionary to store the count of each key press
key_count = {}

# Dictionary to store the count of each mouse click
click_count = {}

# List to store the mouse click locations
click_locations = []

def on_press(key):
    try:
        # Increment the count for the pressed key
        key_count[key] = key_count.get(key, 0) + 1
        print(f"{key}")
    except AttributeError:
        pass

def get_element_name_from_website(url, x, y):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    element = soup.find('html').find_all()[0]  # Example: Assuming the first element on the page
    element_name = element.get_text().strip()

    return element_name


def get_website_name(url):
    parsed_url = urlparse(url)
    website_name = parsed_url.netloc
    return website_name

def on_click(x, y, button, pressed):
    if pressed:
        # Increment the count for the clicked mouse button
        print(f"Mouse button {button} ")

        # Get the name or label of the clicked element on the website
        element_name = get_element_name_from_website('https://example.com', x, y)
        print(f"Clicked element: {element_name}")

def on_release(key):
    if key == keyboard.Key.end:
        # Stop listener on pressing the 'esc' key
        keyboard_listener.stop()
        mouse_listener.stop()
        return False



# Create listeners for keyboard and mouse events
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
mouse_listener = mouse.Listener(on_click=on_click)

# Start the listeners
keyboard_listener.start()
mouse_listener.start()

# Wait for the listeners to finish
keyboard_listener.join()
mouse_listener.join()
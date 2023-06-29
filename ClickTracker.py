from pynput import mouse, keyboard
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_element_name_from_website(url, x, y):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    element = soup.find('html').find_all()[0]  # Example: Assuming the first element on the page
    element_name = element.get_text().strip()

    return element_name

def on_click(x, y, button, pressed):
    if pressed:
        # Increment the count for the clicked mouse button
        print(f"Mouse button {button} ")

        if button == mouse.Button.middle:
            # Stop listener on pressing the scroll wheel button
            mouse_listener.stop()
            return False

        # Get the name or label of the clicked element on the website
        element_name = get_element_name_from_website('https://example.com', x, y)
        print(f"Clicked element: {element_name}")

# Create a listener for mouse clicks
mouse_listener = mouse.Listener(on_click=on_click)

# Start the listener
mouse_listener.start()

# Wait for the listener to finish
mouse_listener.join()


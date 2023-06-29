# InfoLogger
Repository containing key logger and click tracker. Used to track user activity and frequency.

## Introduction:
This ReadMe provides an overview of a Python script that captures and logs keystrokes using the pynput library. The script records key presses and maintains a count of each key encountered. It is essential to note that this script is intended for educational purposes only and should not be used for any malicious activities.

## Dependencies:
a. Python: Ensure that Python is installed on your system.
b. pynput Library: Install the pynput library using the command 'pip install pynput'.

## Script Functionality:
The provided script captures keystrokes in real-time and records them along with their respective frequencies. The keylogger operates as follows:

### Key Capture:

The script uses the pynput.keyboard module to listen for keyboard events, such as key presses and releases.
The 'on_press' function is called whenever a key is pressed.
The 'on_release' function is called whenever a key is released.
### Key Count:

The script maintains a dictionary called 'key_count' to store the count of each key press encountered.
When a key is pressed, the count for that key is incremented in the dictionary.
The dictionary's structure is: {key: count}.
### Script Termination:

Pressing the 'end' key terminates the keylogger script.
The 'on_release' function checks if the key pressed is 'keyboard.Key.end' and returns False to stop the listener.
Usage Instructions:
### Import Dependencies:

Import the 'keyboard' module from the 'pynput' library.
Import any other required libraries or modules specific to your implementation.
### Listener Setup:

Create the necessary functions 'on_press' and 'on_release' to handle key events.
Customize the script to suit your requirements, such as logging the keystrokes to a file or performing additional actions.
### Start and Join the Listener:

Create a keyboard listener using 'keyboard.Listener' and provide the 'on_press' and 'on_release' functions as arguments.
Start the listener by calling the 'start()' method on the keyboard listener object.
Use the 'join()' method to wait for the listener to finish.
### Run the Script:

Execute the script and observe the captured keystrokes and their respective frequencies in the console output.
## Important Note:

It is crucial to use this script responsibly and ensure compliance with legal and ethical guidelines.
Respect user privacy and obtain proper consent before implementing any form of keylogging.
Do not use this script for any malicious purposes or to invade someone's privacy.
## Disclaimer:

This script is provided for educational purposes only. The author disclaim any responsibility for the misuse or illegal use of this script. Use it at your own risk and ensure compliance with applicable laws and regulations.

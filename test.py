import sqlite3
from datetime import datetime

# Connect to SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('input_data.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store character inputs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS character_inputs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character TEXT,
        timestamp TEXT
    )
''')

# Commit changes and close the connection
conn.commit()

# Infinite loop to listen for character inputs
while True:
    # Get input from the user
    user_input = input("Enter characters (or 'exit' to quit): ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        break

    # Split the input string by space and tab
    characters = user_input.split(' ') + user_input.split('\t')

    # Filter out empty entries
    characters = [char for char in characters if char]

    # Get the current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert each character into the database with timestamp (if not duplicate)
    for char in characters:
        cursor.execute('''
            INSERT INTO character_inputs (character, timestamp)
            SELECT ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM character_inputs WHERE character = ? AND timestamp = ?
            )
        ''', (char, current_time, char, current_time))

    # Commit changes
    conn.commit()

# Close the database connection
conn.close()
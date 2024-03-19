import sqlite3

DATABASE = 'community_pantry'


# Connect to the SQLite database (create it if it doesn't exist)
conn = sqlite3.connect(DATABASE)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Read the schema from the schema.sql file and execute it
with open('schema.sql', 'r') as schema_file:
    schema = schema_file.read()
    cursor.execute(schema)

print("Table is created")    

# Commit the changes and close the connection
conn.commit()
conn.close()
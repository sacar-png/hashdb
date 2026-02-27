import sqlite3
import sys

# Connect to the SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('kvstore.db')
cur = conn.cursor()

# Create the table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS kv (
        key TEXT PRIMARY KEY,
        value TEXT
    )
""")
conn.commit()

# Load existing data into an in-memory dictionary
cur.execute("SELECT key, value FROM kv")
store = {row[0]: row[1] for row in cur.fetchall()}

print("Simple Key-Value Store CLI")
print("Commands:")
print("  set <key> <value>  (value can have spaces)")
print("  get <key>")
print("  exit")
print("")

# Interactive loop
while True:
    try:
        cmd = input("> ").strip()
    except EOFError:
        # Handle Ctrl+D or end of input
        break

    if not cmd:
        continue

    parts = cmd.split()
    op = parts[0].lower()

    if op == "set":
        if len(parts) < 3:
            print("Usage: set <key> <value>")
            continue
        key = parts[1]
        value = " ".join(parts[2:])
        # Update in-memory store
        store[key] = value
        # Persist to database
        cur.execute("INSERT OR REPLACE INTO kv (key, value) VALUES (?, ?)", (key, value))
        conn.commit()
        print("OK")

    elif op == "get":
        if len(parts) != 2:
            print("Usage: get <key>")
            continue
        key = parts[1]
        value = store.get(key)
        if value is not None:
            print(value)
        else:
            print("Not found")

    elif op == "exit":
        break

    else:
        print("Unknown command")

# Close the connection
conn.close()
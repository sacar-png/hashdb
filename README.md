# Simple Key-Value Store

This is a basic command-line interface (CLI) key-value store implemented in Python. It uses an in-memory dictionary for fast access and SQLite for persistence, ensuring data is saved to disk.

## Features
- **Set** a key-value pair (values can include spaces).
- **Get** the value for a given key.
- Data is loaded from and saved to a SQLite database (`kvstore.db`).
- Interactive CLI with simple commands.

## Requirements
- Python 3.x
- SQLite3 (included in Python standard library)

## Usage
Run the script:
```
python kvstore.py
```

### Commands
- `set <key> <value>`: Set a key to a value (e.g., `set name John Doe`).
- `get <key>`: Retrieve the value for a key (e.g., `get name`).
- `exit`: Quit the program.

Example session:
```
> set greeting Hello, World!
OK
> get greeting
Hello, World!
> exit
```

## How It Works
- On startup, data is loaded from `kvstore.db` into memory.
- Changes via `set` are updated in memory and persisted to the database.
- The database uses a simple table with `key` (primary) and `value` columns.

## Limitations
- No delete or search operations (simplified version).
- Basic error handling; no transactions beyond single operations.

## License
MIT License. Feel free to use and modify.
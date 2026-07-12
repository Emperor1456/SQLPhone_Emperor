# 📘 SQLPhone Emperor v3.0 · Module 8
# 📖 L80 – Module 8 Capstone: Command‑Line Contact Book

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll build a complete command‑line contact management application using Python and SQLite — integrating every skill from Module 8 into a single, portfolio‑ready project.

- 🧱 **Project structure** – `database.py`, `models.py`, `main.py`
- 🧠 **CRUD operations** – create, read, update, delete contacts
- 🧪 **Error handling** – graceful failure on bad input
- ⚡ **Polished CLI** – argument parsing, user feedback, help text
- 🧰 **Reusable architecture** – this pattern scales directly to web APIs

---

## 🧱 THE IMPERIAL CONTACT BOOK – REQUIREMENTS

A contact manager that runs from the terminal. The user can:
- **Add** a contact (name, phone, email optional, group)
- **List** all contacts alphabetically
- **Search** contacts by name or group
- **Update** a contact’s phone number
- **Delete** a contact by ID

All data persists in a SQLite database.

---

## 🧱 DATABASE LAYER (`database.py`)

```python
import sqlite3

def get_connection(db_path="contacts.db"):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            email TEXT,
            group_name TEXT DEFAULT 'General',
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.commit()
```

---

## 🧱 MODELS (CRUD) – `models.py`

```python
from database import get_connection, create_table

def add_contact(name, phone, email=None, group_name="General"):
    with get_connection() as conn:
        create_table(conn)
        conn.execute(
            "INSERT INTO contacts (name, phone, email, group_name) VALUES (?, ?, ?, ?)",
            (name, phone, email, group_name)
        )
        conn.commit()
    return True

def list_contacts():
    with get_connection() as conn:
        create_table(conn)
        rows = conn.execute("SELECT * FROM contacts ORDER BY name").fetchall()
        return [dict(row) for row in rows]

def search_contacts(query):
    with get_connection() as conn:
        create_table(conn)
        rows = conn.execute(
            "SELECT * FROM contacts WHERE name LIKE ? OR group_name LIKE ?",
            (f"%{query}%", f"%{query}%")
        ).fetchall()
        return [dict(row) for row in rows]

def update_phone(contact_id, new_phone):
    with get_connection() as conn:
        create_table(conn)
        cursor = conn.execute(
            "UPDATE contacts SET phone = ? WHERE id = ?",
            (new_phone, contact_id)
        )
        conn.commit()
        return cursor.rowcount > 0

def delete_contact(contact_id):
    with get_connection() as conn:
        create_table(conn)
        cursor = conn.execute(
            "DELETE FROM contacts WHERE id = ?",
            (contact_id,)
        )
        conn.commit()
        return cursor.rowcount > 0
```

---

## 🧱 CLI – `main.py`

```python
import sys
from models import add_contact, list_contacts, search_contacts, update_phone, delete_contact

def print_usage():
    print("Usage:")
    print("  python main.py add <name> <phone> [email] [group]")
    print("  python main.py list")
    print("  python main.py search <query>")
    print("  python main.py update <id> <new_phone>")
    print("  python main.py delete <id>")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    cmd = sys.argv[1].lower()

    if cmd == "add":
        if len(sys.argv) < 4:
            print("Missing arguments: name and phone required.")
            return
        name, phone = sys.argv[2], sys.argv[3]
        email = sys.argv[4] if len(sys.argv) > 4 else None
        group = sys.argv[5] if len(sys.argv) > 5 else "General"
        add_contact(name, phone, email, group)
        print(f"Contact '{name}' added.")

    elif cmd == "list":
        contacts = list_contacts()
        if not contacts:
            print("No contacts found.")
            return
        for c in contacts:
            print(f"[{c['id']}] {c['name']} - {c['phone']} ({c['group_name']})")

    elif cmd == "search":
        if len(sys.argv) < 3:
            print("Missing search query.")
            return
        results = search_contacts(sys.argv[2])
        if not results:
            print("No matching contacts.")
            return
        for c in results:
            print(f"[{c['id']}] {c['name']} - {c['phone']} ({c['group_name']})")

    elif cmd == "update":
        if len(sys.argv) < 4:
            print("Missing arguments: id and new phone required.")
            return
        success = update_phone(int(sys.argv[2]), sys.argv[3])
        print("Contact updated." if success else "Contact not found.")

    elif cmd == "delete":
        if len(sys.argv) < 3:
            print("Missing argument: id required.")
            return
        success = delete_contact(int(sys.argv[2]))
        print("Contact deleted." if success else "Contact not found.")

    else:
        print(f"Unknown command: {cmd}")
        print_usage()

if __name__ == "__main__":
    main()
```

---

## 💡 Real‑world Usage

This architecture directly mirrors production backend services:
- `database.py` = connection layer
- `models.py` = business logic (CRUD)
- `main.py` = presentation layer (CLI or API)

Replace `main.py` with a Flask/FastAPI app, and you have a REST API.

---

## 🔍 Practice Preview
You will build the Command‑Line Contact Book from scratch.

| Level | Task |
|-------|------|
| Easy | Create the `contacts` table and insert a contact from Python. |
| Medium | Build the `list` and `delete` functions. |
| Hard | Assemble the full CLI with argument parsing and test all five operations. |

Run the coach:
```bash
python ii_Practice_Sheets/L80_Module_8_Capstone_Command_Line_Contact_Book.py
```

---

## 📌 Key Takeaway
- A complete application combines a database layer, business logic, and a user interface.  
- CRUD operations are the backbone of any data‑driven app.  
- This pattern scales directly to web backends and REST APIs.  
- You now have a portfolio‑ready project you built entirely on a phone.

*For Emperor.*
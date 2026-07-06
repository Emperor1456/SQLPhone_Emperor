# 📘 SQLPhone Emperor · SQL Module 09
# 📖 L‑80 – Mini‑Project: Contact Book

## 🎯 OBJECTIVE
Build a command‑line contact book using Python and SQLite.

## 🧱 BRICK 1 – Features
- Add contact (name, phone, email)
- List all contacts
- Search by name
- Update phone number
- Delete contact

Store data in a local `contacts.db` file.

## 🧱 BRICK 2 – Implementation Outline
1. Create a table with appropriate constraints.
2. Provide a menu loop with user choices.
3. Use parameterized queries for all operations.
4. Handle errors (e.g., duplicate email).
5. Optionally, export to CSV.

```python
def add_contact(db):
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')
    db.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
    print('Contact added.')
```
Repeat for other functions.

## 💡 Why This Matters
A contact book is a real, usable application.
It combines all Module‑09 skills into one project.
You can extend it later with categories, search, etc.

## 📌 Key Takeaway
Build something tangible.
A contact book proves you can create data‑driven apps.
It’s small, but it’s yours.

*From lessons to software – you are an engineer now.*
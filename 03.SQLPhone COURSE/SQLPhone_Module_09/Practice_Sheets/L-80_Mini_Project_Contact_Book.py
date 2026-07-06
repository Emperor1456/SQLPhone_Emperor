# L-80_Mini_Project_Contact_Book.py
# SQLPhone Emperor – SQL Module 09
# Practice: Build the contact book CLI.

import sqlite3, os

DB = "contacts_test.db"

def task():
    print("=" * 50)
    print("🧱 MINI‑PROJECT: Contact Book")
    print("Create a complete contact book app with add, list, search, update, delete.")
    print("Your Python script should manage 'contacts.db' with a menu loop.")
    print("We'll run your script and check if the database contains a test entry you'll insert.")
    print("=" * 50)
    if os.path.exists(DB):
        os.remove(DB)
    user_code = input("Paste your full script (will be saved to temp and run):\n")
    with open("contact_app.py", "w") as f:
        f.write(user_code)
    import subprocess
    # Run the script with input "1\nTest\n123\ntest@test.com\n5\n" to add then exit
    proc = subprocess.run(["python", "contact_app.py"], input="1\nEmperor\n000\ne@e.com\n5\n", text=True, capture_output=True)
    # Check db
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    try:
        cur.execute("SELECT name FROM contacts WHERE name='Emperor'")
        row = cur.fetchone()
        if row:
            print("✅ Contact 'Emperor' found. Your contact book works!")
            conn.close()
            os.unlink("contact_app.py")
            os.unlink(DB)
            return True
        else:
            print("❌ Contact not found. Did you add via menu?")
            conn.close()
            os.unlink("contact_app.py")
            os.unlink(DB)
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        os.unlink("contact_app.py")
        if os.path.exists(DB): os.unlink(DB)
        return False

def main():
    while True:
        if task():
            break
        retry = input("Try again? (y/n): ")
        if retry.lower() != 'y':
            break

if __name__ == "__main__":
    main()
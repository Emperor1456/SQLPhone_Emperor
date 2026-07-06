# L-75_UPDATE_and_DELETE_with_Python.py
# SQLPhone Emperor – SQL Module 09
# Practice: Update and delete rows.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Table 'scores' (player TEXT, points INT) exists with some data (we'll create).")
    print("Write Python code to update the points of a specific player and then delete another player.")
    print("Use parameterized queries.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE scores (player TEXT, points INT)")
    conn.executemany("INSERT INTO scores VALUES (?, ?)", [('Alice', 100), ('Bob', 200), ('Charlie', 150)])
    conn.commit()
    user_code = input(">>> ")
    try:
        exec(user_code, {"conn": conn})
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    # Check that update and delete happened
    cur = conn.cursor()
    cur.execute("SELECT player, points FROM scores WHERE player='Alice'")
    alice = cur.fetchone()
    cur.execute("SELECT player FROM scores WHERE player='Bob'")
    bob = cur.fetchone()
    if alice and alice[1] != 100 and bob is None:
        print(f"✅ Alice updated to {alice[1]}, Bob deleted.")
        conn.close()
        return True
    else:
        print(f"❌ Expected Alice updated (not 100) and Bob gone. Alice: {alice}, Bob: {bob}")
        conn.close()
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
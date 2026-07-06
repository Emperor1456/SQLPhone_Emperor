# L-36_Joining_More_Than_Two_Tables.py
# SQLPhone Emperor – SQL Module 04
# Practice: Join three or more tables.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create tables 'authors' (id, name), 'books' (id, title, author_id), 'reviews' (id, book_id, reviewer_name).")
    print("Insert data. Write a query that returns book title, author name, and reviewer name for all reviews.")
    print("(Requires joining authors->books->reviews).")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your SQL:\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        cur.execute("SELECT COUNT(*) FROM reviews")
        review_count = cur.fetchone()[0]
        cur.execute("""
            SELECT b.title, a.name, r.reviewer_name
            FROM reviews r
            JOIN books b ON r.book_id = b.id
            JOIN authors a ON b.author_id = a.id
        """)
        rows = cur.fetchall()
        if len(rows) == review_count:
            print(f"✅ Three‑table join returned all {review_count} reviews.")
            conn.close()
            return True
        else:
            print(f"❌ Expected {review_count} rows, got {len(rows)}. Check joins.")
            conn.close()
            return False
    except Exception as e:
        print(f"❌ Verification error: {e}")
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
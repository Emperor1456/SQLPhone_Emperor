# L-11_SELECT_DISTINCT.py
# SQLPhone Emperor – SQL Module 02
# Practice: Using SELECT DISTINCT.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'orders' (id, customer_name, city, country).")
    print("Insert multiple rows, some with duplicate city/country pairs.")
    print("Write a query that returns all unique city/country pairs.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your SQL (DDL + INSERT + query):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False

    try:
        cur.execute("SELECT COUNT(*) FROM orders")
        total = cur.fetchone()[0]
        if total < 2:
            print("❌ Need at least 2 rows.")
            conn.close()
            return False
        cur.execute("SELECT COUNT(*) FROM (SELECT DISTINCT city, country FROM orders)")
        unique = cur.fetchone()[0]
        if unique >= total:
            print("❌ No duplicate city/country pairs found. Insert at least one duplicate pair.")
            conn.close()
            return False
        else:
            print(f"✅ Table has {total} rows, {unique} unique city/country pairs.")
            print("Your DISTINCT query should return the unique ones.")
            conn.close()
            return True
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
    main()# L-12_WHERE_Clause.py
# SQLPhone Emperor – SQL Module 02
# Practice: Filter rows with comparison operators.

import sqlite3

def task():
    print("=" * 50)
    print("🧱 TASK: Create table 'products' (id, name, price, stock).")
    print("Insert at least 3 rows with varied prices and stocks.")
    print("Write a SELECT that returns products with price > 20 AND stock > 0.")
    print("=" * 50)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    user_sql = input("Enter your SQL (DDL + DML + query):\n> ")
    try:
        cur.executescript(user_sql)
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()
        return False
    try:
        cur.execute("SELECT COUNT(*) FROM products WHERE price > 20 AND stock > 0")
        count = cur.fetchone()[0]
        if count > 0:
            print(f"✅ Query found {count} matching products.")
            conn.close()
            return True
        else:
            print("❌ No rows satisfy price > 20 AND stock > 0. Adjust data or query.")
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
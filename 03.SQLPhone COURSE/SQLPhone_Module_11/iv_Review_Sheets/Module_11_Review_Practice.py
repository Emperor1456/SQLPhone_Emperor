import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

# ─── Easy: Build two related tables ─────────────────
def verify_easy(cur, conn):
    for tbl in ['doctors', 'patients']:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tbl}'")
        if not cur.fetchone():
            return False
    cur.execute("SELECT COUNT(*) FROM doctors")
    if cur.fetchone()[0] < 2: return False
    cur.execute("SELECT COUNT(*) FROM patients")
    return cur.fetchone()[0] >= 2

easy = Task(
    description="Create tables:\n"
                "  doctors (id INTEGER PRIMARY KEY, name TEXT, specialty TEXT)\n"
                "  patients (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)\n"
                "Insert at least 2 doctors and 2 patients.",
    verify_func=verify_easy,
    level=Level.EASY,
    hints=[
        "CREATE TABLE doctors (id INTEGER PRIMARY KEY, name TEXT, specialty TEXT);",
        "CREATE TABLE patients (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);",
        "INSERT INTO doctors VALUES (1,'Dr. Smith','Cardiology'), (2,'Dr. Lee','Neurology');",
        "INSERT INTO patients VALUES (1,'Alice',30), (2,'Bob',45);"
    ]
)

# ─── Medium: Add appointments with JOIN ─────────────
def verify_medium(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='appointments'")
    if not cur.fetchone():
        return False
    cur.execute("SELECT COUNT(*) FROM appointments")
    if cur.fetchone()[0] < 2: return False
    # Verify a join query works
    cur.execute("""
        SELECT p.name, d.name, a.appt_date
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
        JOIN doctors d ON a.doctor_id = d.id
    """)
    return len(cur.fetchall()) >= 2

medium = Task(
    description="Add table 'appointments' (id INTEGER PRIMARY KEY, patient_id INTEGER, doctor_id INTEGER,\n"
                "  appt_date TEXT, FOREIGN KEYs to patients and doctors).\n"
                "Insert at least 2 appointments linking existing patients and doctors.\n"
                "Write a query that shows patient name, doctor name, and appointment date.",
    verify_func=verify_medium,
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE appointments (id INTEGER PRIMARY KEY, patient_id INTEGER, doctor_id INTEGER, appt_date TEXT, FOREIGN KEY(patient_id) REFERENCES patients(id), FOREIGN KEY(doctor_id) REFERENCES doctors(id));",
        "INSERT INTO appointments VALUES (1,1,1,'2026-08-01'), (2,2,2,'2026-08-02');",
        "SELECT p.name, d.name, a.appt_date FROM appointments a JOIN patients p ON a.patient_id=p.id JOIN doctors d ON a.doctor_id=d.id;"
    ]
)

# ─── Hard: Full hospital report with aggregation and CASE ─
def verify_hard(cur, conn):
    # Verify required tables
    for tbl in ['doctors','patients','appointments','prescriptions']:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tbl}'")
        if not cur.fetchone():
            return False
    cur.execute("SELECT COUNT(*) FROM prescriptions")
    if cur.fetchone()[0] < 2: return False

    expected = "Dr. Smith 2 185.00\nDr. Lee 1 70.00"
    cur.execute("""
        SELECT d.name, COUNT(a.id) AS appointments,
               COALESCE(SUM(p.cost), 0) AS total_revenue
        FROM doctors d
        JOIN appointments a ON d.id = a.doctor_id
        LEFT JOIN prescriptions p ON a.id = p.appointment_id
        GROUP BY d.name
        ORDER BY d.name
    """)
    rows = cur.fetchall()
    result = "\n".join(f"{r[0]} {r[1]} {r[2]:.2f}" for r in rows)
    return result == expected

hard = Task(
    description="Hospital Management System – Final Report\n\n"
                "Build the complete schema:\n"
                "1. Reuse/ensure 'doctors' and 'patients' tables exist with at least 2 rows each.\n"
                "2. Ensure 'appointments' table exists with at least 2 rows.\n"
                "3. Create table 'prescriptions' (id INTEGER PRIMARY KEY, appointment_id INTEGER,\n"
                "   drug TEXT, cost REAL, FOREIGN KEY(appointment_id) REFERENCES appointments(id)).\n"
                "4. Insert prescriptions:\n"
                "   (1,1,'Aspirin',50.00), (2,1,'Ibuprofen',35.00), (3,2,'Paracetamol',70.00).\n"
                "   (This means appointment 1 has two prescriptions, appointment 2 has one.)\n"
                "5. Write a report that shows:\n"
                "   - Doctor name\n"
                "   - Total number of appointments for that doctor\n"
                "   - Total revenue from prescriptions (sum of cost) for that doctor\n"
                "   Group by doctor name, sort by name.\n"
                "   Use COALESCE to show 0 if no prescriptions.\n\n"
                "Expected output:\n"
                "Dr. Smith 2 185.00\n"
                "Dr. Lee 1 70.00",
    verify_func=verify_hard,
    level=Level.HARD,
    hints=[
        "CREATE TABLE IF NOT EXISTS doctors (id INTEGER PRIMARY KEY, name TEXT, specialty TEXT);",
        "INSERT OR IGNORE INTO doctors VALUES (1,'Dr. Smith','Cardiology'), (2,'Dr. Lee','Neurology');",
        "CREATE TABLE IF NOT EXISTS patients (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);",
        "INSERT OR IGNORE INTO patients VALUES (1,'Alice',30), (2,'Bob',45);",
        "CREATE TABLE IF NOT EXISTS appointments (id INTEGER PRIMARY KEY, patient_id INTEGER, doctor_id INTEGER, appt_date TEXT, FOREIGN KEY(patient_id) REFERENCES patients(id), FOREIGN KEY(doctor_id) REFERENCES doctors(id));",
        "INSERT OR IGNORE INTO appointments VALUES (1,1,1,'2026-08-01'), (2,2,2,'2026-08-02');",
        "CREATE TABLE prescriptions (id INTEGER PRIMARY KEY, appointment_id INTEGER, drug TEXT, cost REAL, FOREIGN KEY(appointment_id) REFERENCES appointments(id));",
        "INSERT INTO prescriptions VALUES (1,1,'Aspirin',50.0), (2,1,'Ibuprofen',35.0), (3,2,'Paracetamol',70.0);",
        "SELECT d.name, COUNT(a.id), COALESCE(SUM(p.cost),0) FROM doctors d JOIN appointments a ON d.id=a.doctor_id LEFT JOIN prescriptions p ON a.id=p.appointment_id GROUP BY d.name ORDER BY d.name;"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()

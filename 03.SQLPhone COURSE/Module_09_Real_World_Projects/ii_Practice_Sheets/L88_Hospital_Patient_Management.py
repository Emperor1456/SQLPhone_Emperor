import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏥  Imperial Hospital – Build the Schema\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates the four tables:\n"
        "     doctors, patients, appointments, prescriptions\n"
        "     (exact schema from the lecture).\n"
        "  3. Inserts seed data:\n"
        "     • Doctors: (1,'Dr. Karim','Cardiology'),\n"
        "       (2,'Dr. Begum','Neurology')\n"
        "     • Patients: (1,'Emperor','2008-07-10','01710000000'),\n"
        "       (2,'Rahim','1995-03-22','01720000000')\n"
        "     • Appointments:\n"
        "       (1,1,1,'2026-07-15','Routine checkup'),\n"
        "       (2,2,2,'2026-07-15','Headache consultation'),\n"
        "       (3,1,1,'2026-08-01','Follow-up')\n"
        "     • Prescriptions:\n"
        "       (1,1,'Aspirin','75mg daily'),\n"
        "       (2,2,'Ibuprofen','200mg as needed'),\n"
        "       (3,3,'Aspirin','75mg daily')\n"
        "  4. Commits, then SELECTs all doctor names\n"
        "     sorted alphabetically and prints them.\n\n"
        "Expected output:\n[('Dr. Begum',), ('Dr. Karim',)]"
    ),
    expected_output="[('Dr. Begum',), ('Dr. Karim',)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''",
        "CREATE TABLE doctors (doctor_id INTEGER PRIMARY KEY, name TEXT NOT NULL, specialty TEXT);",
        "CREATE TABLE patients (patient_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dob TEXT, contact TEXT);",
        "CREATE TABLE appointments (appt_id INTEGER PRIMARY KEY, patient_id INTEGER, doctor_id INTEGER, appt_date TEXT, notes TEXT, FOREIGN KEY (patient_id) REFERENCES patients(patient_id), FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id));",
        "CREATE TABLE prescriptions (presc_id INTEGER PRIMARY KEY, appt_id INTEGER, drug TEXT NOT NULL, dosage TEXT, FOREIGN KEY (appt_id) REFERENCES appointments(appt_id));",
        "''')",
        "conn.executescript('''",
        "INSERT INTO doctors VALUES (1,'Dr. Karim','Cardiology'), (2,'Dr. Begum','Neurology');",
        "INSERT INTO patients VALUES (1,'Emperor','2008-07-10','01710000000'), (2,'Rahim','1995-03-22','01720000000');",
        "INSERT INTO appointments VALUES (1,1,1,'2026-07-15','Routine checkup'), (2,2,2,'2026-07-15','Headache consultation'), (3,1,1,'2026-08-01','Follow-up');",
        "INSERT INTO prescriptions VALUES (1,1,'Aspirin','75mg daily'), (2,2,'Ibuprofen','200mg as needed'), (3,3,'Aspirin','75mg daily');",
        "''')",
        "conn.commit()",
        "cursor = conn.execute('SELECT name FROM doctors ORDER BY name')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "📋  All Patients – Quick List\n\n"
        "The hospital database is seeded.\n"
        "Write Python code that lists each patient's name\n"
        "and contact, sorted by name.\n\n"
        "Expected output:\n[('Emperor','01710000000'), ('Rahim','01720000000')]"
    ),
    setup_sql=(
        "CREATE TABLE doctors (doctor_id INTEGER PRIMARY KEY, name TEXT NOT NULL, specialty TEXT);"
        "INSERT INTO doctors VALUES (1,'Dr. Karim','Cardiology'), (2,'Dr. Begum','Neurology');"
        "CREATE TABLE patients (patient_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dob TEXT, contact TEXT);"
        "INSERT INTO patients VALUES (1,'Emperor','2008-07-10','01710000000'), (2,'Rahim','1995-03-22','01720000000');"
        "CREATE TABLE appointments (appt_id INTEGER PRIMARY KEY, patient_id INTEGER, doctor_id INTEGER, appt_date TEXT, notes TEXT, FOREIGN KEY (patient_id) REFERENCES patients(patient_id), FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id));"
        "INSERT INTO appointments VALUES (1,1,1,'2026-07-15','Routine checkup'), (2,2,2,'2026-07-15','Headache consultation'), (3,1,1,'2026-08-01','Follow-up');"
        "CREATE TABLE prescriptions (presc_id INTEGER PRIMARY KEY, appt_id INTEGER, drug TEXT NOT NULL, dosage TEXT, FOREIGN KEY (appt_id) REFERENCES appointments(appt_id));"
        "INSERT INTO prescriptions VALUES (1,1,'Aspirin','75mg daily'), (2,2,'Ibuprofen','200mg as needed'), (3,3,'Aspirin','75mg daily');"
    ),
    expected_output="[('Emperor', '01710000000'), ('Rahim', '01720000000')]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('SELECT name, contact FROM patients ORDER BY name')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📅  Today's Appointments – July 15, 2026\n\n"
        "The hospital database is seeded.\n"
        "Write Python code that lists all appointments on\n"
        "'2026-07-15', showing patient name, doctor name,\n"
        "specialty, and notes. Sort by patient name.\n\n"
        "Expected output:\n[('Emperor','Dr. Karim','Cardiology','Routine checkup'), ('Rahim','Dr. Begum','Neurology','Headache consultation')]"
    ),
    setup_sql=(
        "CREATE TABLE doctors (doctor_id INTEGER PRIMARY KEY, name TEXT NOT NULL, specialty TEXT);"
        "INSERT INTO doctors VALUES (1,'Dr. Karim','Cardiology'), (2,'Dr. Begum','Neurology');"
        "CREATE TABLE patients (patient_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dob TEXT, contact TEXT);"
        "INSERT INTO patients VALUES (1,'Emperor','2008-07-10','01710000000'), (2,'Rahim','1995-03-22','01720000000');"
        "CREATE TABLE appointments (appt_id INTEGER PRIMARY KEY, patient_id INTEGER, doctor_id INTEGER, appt_date TEXT, notes TEXT, FOREIGN KEY (patient_id) REFERENCES patients(patient_id), FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id));"
        "INSERT INTO appointments VALUES (1,1,1,'2026-07-15','Routine checkup'), (2,2,2,'2026-07-15','Headache consultation'), (3,1,1,'2026-08-01','Follow-up');"
        "CREATE TABLE prescriptions (presc_id INTEGER PRIMARY KEY, appt_id INTEGER, drug TEXT NOT NULL, dosage TEXT, FOREIGN KEY (appt_id) REFERENCES appointments(appt_id));"
        "INSERT INTO prescriptions VALUES (1,1,'Aspirin','75mg daily'), (2,2,'Ibuprofen','200mg as needed'), (3,3,'Aspirin','75mg daily');"
    ),
    expected_output="[('Emperor', 'Dr. Karim', 'Cardiology', 'Routine checkup'), ('Rahim', 'Dr. Begum', 'Neurology', 'Headache consultation')]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT p.name, d.name, d.specialty, a.notes",
        "FROM appointments a JOIN patients p ON a.patient_id = p.patient_id",
        "JOIN doctors d ON a.doctor_id = d.doctor_id",
        "WHERE a.appt_date = '2026-07-15' ORDER BY p.name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "💊  Patient Prescription History – Emperor\n\n"
        "The hospital database is seeded.\n"
        "Write Python code that retrieves Emperor’s\n"
        "(patient_id=1) prescription history: appointment\n"
        "date, doctor name, drug, and dosage. Sort by\n"
        "appointment date descending.\n\n"
        "Expected output:\n[('2026-08-01','Dr. Karim','Aspirin','75mg daily'), ('2026-07-15','Dr. Karim','Aspirin','75mg daily')]"
    ),
    setup_sql=(
        "CREATE TABLE doctors (doctor_id INTEGER PRIMARY KEY, name TEXT NOT NULL, specialty TEXT);"
        "INSERT INTO doctors VALUES (1,'Dr. Karim','Cardiology'), (2,'Dr. Begum','Neurology');"
        "CREATE TABLE patients (patient_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dob TEXT, contact TEXT);"
        "INSERT INTO patients VALUES (1,'Emperor','2008-07-10','01710000000'), (2,'Rahim','1995-03-22','01720000000');"
        "CREATE TABLE appointments (appt_id INTEGER PRIMARY KEY, patient_id INTEGER, doctor_id INTEGER, appt_date TEXT, notes TEXT, FOREIGN KEY (patient_id) REFERENCES patients(patient_id), FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id));"
        "INSERT INTO appointments VALUES (1,1,1,'2026-07-15','Routine checkup'), (2,2,2,'2026-07-15','Headache consultation'), (3,1,1,'2026-08-01','Follow-up');"
        "CREATE TABLE prescriptions (presc_id INTEGER PRIMARY KEY, appt_id INTEGER, drug TEXT NOT NULL, dosage TEXT, FOREIGN KEY (appt_id) REFERENCES appointments(appt_id));"
        "INSERT INTO prescriptions VALUES (1,1,'Aspirin','75mg daily'), (2,2,'Ibuprofen','200mg as needed'), (3,3,'Aspirin','75mg daily');"
    ),
    expected_output="[('2026-08-01', 'Dr. Karim', 'Aspirin', '75mg daily'), ('2026-07-15', 'Dr. Karim', 'Aspirin', '75mg daily')]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT a.appt_date, d.name, pr.drug, pr.dosage",
        "FROM prescriptions pr JOIN appointments a ON pr.appt_id = a.appt_id",
        "JOIN doctors d ON a.doctor_id = d.doctor_id",
        "WHERE a.patient_id = 1 ORDER BY a.appt_date DESC",
        "''')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📊  Monthly Doctor Workload – July 2026\n\n"
        "The hospital database is seeded.\n"
        "Write Python code that counts each doctor's\n"
        "appointments in July 2026. Show doctor name\n"
        "and appointment count, sorted by name.\n"
        "Include doctors with zero appointments.\n\n"
        "Expected output:\n[('Dr. Begum',1), ('Dr. Karim',1)]"
    ),
    setup_sql=(
        "CREATE TABLE doctors (doctor_id INTEGER PRIMARY KEY, name TEXT NOT NULL, specialty TEXT);"
        "INSERT INTO doctors VALUES (1,'Dr. Karim','Cardiology'), (2,'Dr. Begum','Neurology');"
        "CREATE TABLE patients (patient_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dob TEXT, contact TEXT);"
        "INSERT INTO patients VALUES (1,'Emperor','2008-07-10','01710000000'), (2,'Rahim','1995-03-22','01720000000');"
        "CREATE TABLE appointments (appt_id INTEGER PRIMARY KEY, patient_id INTEGER, doctor_id INTEGER, appt_date TEXT, notes TEXT, FOREIGN KEY (patient_id) REFERENCES patients(patient_id), FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id));"
        "INSERT INTO appointments VALUES (1,1,1,'2026-07-15','Routine checkup'), (2,2,2,'2026-07-15','Headache consultation'), (3,1,1,'2026-08-01','Follow-up');"
        "CREATE TABLE prescriptions (presc_id INTEGER PRIMARY KEY, appt_id INTEGER, drug TEXT NOT NULL, dosage TEXT, FOREIGN KEY (appt_id) REFERENCES appointments(appt_id));"
        "INSERT INTO prescriptions VALUES (1,1,'Aspirin','75mg daily'), (2,2,'Ibuprofen','200mg as needed'), (3,3,'Aspirin','75mg daily');"
    ),
    expected_output="[('Dr. Begum', 1), ('Dr. Karim', 1)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT d.name, COUNT(a.appt_id) AS appointments",
        "FROM doctors d LEFT JOIN appointments a ON d.doctor_id = a.doctor_id",
        "   AND strftime('%Y-%m', a.appt_date) = '2026-07'",
        "GROUP BY d.doctor_id ORDER BY d.name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "💊  Most Prescribed Drug\n\n"
        "The hospital database is seeded.\n"
        "Write Python code that finds the most prescribed\n"
        "drug (the drug with the highest count).\n"
        "Show drug name and count. If there is a tie,\n"
        "return the first one alphabetically.\n\n"
        "Expected output:\n[('Aspirin',2)]"
    ),
    setup_sql=(
        "CREATE TABLE doctors (doctor_id INTEGER PRIMARY KEY, name TEXT NOT NULL, specialty TEXT);"
        "INSERT INTO doctors VALUES (1,'Dr. Karim','Cardiology'), (2,'Dr. Begum','Neurology');"
        "CREATE TABLE patients (patient_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dob TEXT, contact TEXT);"
        "INSERT INTO patients VALUES (1,'Emperor','2008-07-10','01710000000'), (2,'Rahim','1995-03-22','01720000000');"
        "CREATE TABLE appointments (appt_id INTEGER PRIMARY KEY, patient_id INTEGER, doctor_id INTEGER, appt_date TEXT, notes TEXT, FOREIGN KEY (patient_id) REFERENCES patients(patient_id), FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id));"
        "INSERT INTO appointments VALUES (1,1,1,'2026-07-15','Routine checkup'), (2,2,2,'2026-07-15','Headache consultation'), (3,1,1,'2026-08-01','Follow-up');"
        "CREATE TABLE prescriptions (presc_id INTEGER PRIMARY KEY, appt_id INTEGER, drug TEXT NOT NULL, dosage TEXT, FOREIGN KEY (appt_id) REFERENCES appointments(appt_id));"
        "INSERT INTO prescriptions VALUES (1,1,'Aspirin','75mg daily'), (2,2,'Ibuprofen','200mg as needed'), (3,3,'Aspirin','75mg daily');"
    ),
    expected_output="[('Aspirin', 2)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT drug, COUNT(*) AS cnt FROM prescriptions",
        "GROUP BY drug ORDER BY cnt DESC, drug ASC LIMIT 1",
        "''')",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L88.json",
        module_name="Module_09_Real_World_Projects",
        lesson_name="L88_Hospital_Patient_Management"
    )
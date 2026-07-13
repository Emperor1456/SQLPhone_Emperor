import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
SELECT p.name, d.name, a.notes
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors d ON a.doctor_id = d.doctor_id
WHERE a.appt_date = '2026-07-15'
ORDER BY p.name;"""

EXPECTED = "[('Emperor', 'Dr. Karim', 'Routine checkup'), ('Rahim', 'Dr. Begum', 'Headache consultation')]"

SETUP = """\
CREATE TABLE doctors (doctor_id INTEGER PRIMARY KEY, name TEXT NOT NULL, specialty TEXT);
INSERT INTO doctors VALUES (1,'Dr. Karim','Cardiology'), (2,'Dr. Begum','Neurology');
CREATE TABLE patients (patient_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dob TEXT, contact TEXT);
INSERT INTO patients VALUES (1,'Emperor','2008-07-10','01710000000'), (2,'Rahim','1995-03-22','01720000000');
CREATE TABLE appointments (appt_id INTEGER PRIMARY KEY, patient_id INTEGER, doctor_id INTEGER, appt_date TEXT, notes TEXT, FOREIGN KEY (patient_id) REFERENCES patients(patient_id), FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id));
INSERT INTO appointments VALUES (1,1,1,'2026-07-15','Routine checkup'), (2,2,2,'2026-07-15','Headache consultation'), (3,1,1,'2026-08-01','Follow-up');"""

HINTS = [
    "The query looks fine, but the second JOIN uses an alias 'd' which is defined as doctors, but the table might be misspelled in the FROM clause.",
    "Check the spelling of 'appointments' – it might be 'appoitments'.",
    "Correct the spelling of 'appoitments' to 'appointments'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L88 – Hospital Patient Management",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )

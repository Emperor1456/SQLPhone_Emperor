# 📘 SQLPhone Emperor v3.0 · Module 9
# 📖 L88 – Hospital Patient Management

---

## 🎯 OBJECTIVE — What You Will Master

> Build a complete hospital database with patients, doctors, appointments, and prescriptions — integrating scheduling, medical history, and workload reporting into a single system.

- 🧱 **Tables** – patients, doctors, appointments, prescriptions
- 🧠 **Constraints** – unique appointment slots, drug dosage rules
- 🧪 **Reports** – daily appointment list, patient prescription history, doctor workload
- ⚡ **Real‑world** – EHR (Electronic Health Record) systems, clinic management

---

## 🧱 THE IMPERIAL HOSPITAL – BUSINESS REQUIREMENT

The Imperial Hospital schedules patient appointments with doctors. Each appointment may produce prescriptions. The hospital administration needs:
- Today’s appointment list (patient name, doctor, time)
- A full prescription history for any patient
- Monthly workload per doctor (appointment count)
- Patients who haven’t visited in over a year

---

## 🧱 SCHEMA

```sql
CREATE TABLE doctors (
    doctor_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    specialty TEXT
);

CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dob TEXT,
    contact TEXT
);

CREATE TABLE appointments (
    appt_id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    doctor_id INTEGER,
    appt_date TEXT,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE prescriptions (
    presc_id INTEGER PRIMARY KEY,
    appt_id INTEGER,
    drug TEXT NOT NULL,
    dosage TEXT,
    FOREIGN KEY (appt_id) REFERENCES appointments(appt_id)
);
```

---

## 🧱 SEED DATA

```sql
INSERT INTO doctors VALUES (1, 'Dr. Karim', 'Cardiology'), (2, 'Dr. Begum', 'Neurology');
INSERT INTO patients VALUES (1, 'Emperor', '2008-07-10', '01710000000'), (2, 'Rahim', '1995-03-22', '01720000000');
INSERT INTO appointments VALUES (1, 1, 1, '2026-07-15', 'Routine checkup'), (2, 2, 2, '2026-07-15', 'Headache consultation');
INSERT INTO prescriptions VALUES (1, 1, 'Aspirin', '75mg daily'), (2, 2, 'Ibuprofen', '200mg as needed');
```

---

## 🧱 KEY QUERIES

**① Today’s appointments**
```sql
SELECT p.name AS patient, d.name AS doctor, d.specialty, a.appt_date, a.notes
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors d ON a.doctor_id = d.doctor_id
WHERE date(a.appt_date) = date('now');
```

**② Patient prescription history**
```sql
SELECT a.appt_date, d.name AS doctor, pr.drug, pr.dosage
FROM prescriptions pr
JOIN appointments a ON pr.appt_id = a.appt_id
JOIN doctors d ON a.doctor_id = d.doctor_id
WHERE a.patient_id = 1
ORDER BY a.appt_date DESC;
```

**③ Monthly doctor workload**
```sql
SELECT d.name,
       COUNT(a.appt_id) AS appointments
FROM doctors d
LEFT JOIN appointments a ON d.doctor_id = a.doctor_id
   AND strftime('%Y-%m', a.appt_date) = strftime('%Y-%m', 'now')
GROUP BY d.doctor_id;
```

**④ Patients with no appointments in the last 12 months**
```sql
SELECT p.name
FROM patients p
WHERE p.patient_id NOT IN (
    SELECT patient_id FROM appointments
    WHERE appt_date >= date('now', '-1 year')
);
```

**⑤ Most prescribed drugs**
```sql
SELECT drug, COUNT(*) AS times_prescribed
FROM prescriptions
GROUP BY drug
ORDER BY times_prescribed DESC;
```

> 💡 **INSIGHT:** The `appointments` table is the central hub — it links patients to doctors and drives prescriptions. This star‑schema pattern is common in operational databases.

> ⚠️ **WARNING:** In a real hospital system, you would add a `UNIQUE` constraint on `(doctor_id, appt_date)` to prevent double‑booking. SQLite’s conflict resolution can handle this elegantly.

---

## 💡 Real‑world Usage

- Hospital management software
- Clinic scheduling systems
- Telemedicine platforms
- Veterinary clinics

---

## 🔍 Practice Preview
You will build a hospital management database.

| Level | Task |
|-------|------|
| Easy | Create tables and insert seed data. |
| Medium | Write a query listing today’s appointments with patient and doctor names. |
| Hard | Retrieve the full prescription history for a given patient, then find the most prescribed drug across all patients. |

Run the coach:
```bash
python ii_Practice_Sheets/L88_Hospital_Patient_Management.py
```

---

## 📌 Key Takeaway
- Appointments link patients and doctors; prescriptions link to appointments.
- Date filtering is critical for daily schedules and inactivity detection.
- Aggregation and grouping produce workload and drug‑popularity reports.

*For Emperor.*
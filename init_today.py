import sqlite3
from datetime import date

today = date.today().isoformat()

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("SELECT id FROM students")
students = cursor.fetchall()

for (sid,) in students:
    cursor.execute("""
    INSERT OR IGNORE INTO attendance (date, student_id, status)
    VALUES (?, ?, 'Absent')
    """, (today, sid))

conn.commit()
conn.close()

print(f"✅ Attendance initialized for {today}")

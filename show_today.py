import sqlite3
from datetime import date

today = date.today().isoformat()
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("""
SELECT s.id, s.name, a.status
FROM attendance a
JOIN students s ON s.id = a.student_id
WHERE a.date = ?
""", (today,))

rows = cursor.fetchall()
conn.close()

print(f"\n📅 Attendance for {today}\n")
for r in rows:
    print(r)

import sqlite3
from datetime import date

def mark_present(student_id):
    today = date.today().isoformat()

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE attendance
    SET status = 'Present'
    WHERE date = ? AND student_id = ?
    """, (today, student_id))

    conn.commit()
    conn.close()

    return f"✅ Attendance marked for {student_id} on {today}"

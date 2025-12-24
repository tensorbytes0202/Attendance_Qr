import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id TEXT PRIMARY KEY,
    name TEXT
)
""")

# Attendance table (DATE WISE)
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    date TEXT,
    student_id TEXT,
    status TEXT,
    PRIMARY KEY (date, student_id)
)
""")

conn.commit()
conn.close()

print("✅ Database & tables created")

import sqlite3

students = [
    ("202501", "Aditya"),
    ("202502", "Rahul"),
    ("202503", "Sneha")
]

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

for s in students:
    cursor.execute(
        "INSERT OR IGNORE INTO students VALUES (?, ?)", s
    )

conn.commit()
conn.close()

print("✅ Students inserted")

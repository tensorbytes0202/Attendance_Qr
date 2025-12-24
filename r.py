import cv2
import sqlite3
from datetime import date

# ================= DATABASE =================
DB_PATH = "attendance.db"
today = date.today().isoformat()

def init_today_attendance():
    conn = sqlite3.connect(DB_PATH)
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

# ================= MARK PRESENT =================
def mark_present(student_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT status FROM attendance
    WHERE date=? AND student_id=?
    """, (today, student_id))

    row = cursor.fetchone()

    if row is None:
        msg = "❌ Student not found"
    elif row[0] == "Present":
        msg = f"⚠️ ID {student_id} already Present"
    else:
        cursor.execute("""
        UPDATE attendance
        SET status='Present'
        WHERE date=? AND student_id=?
        """, (today, student_id))
        conn.commit()
        msg = f"✅ Attendance marked for {student_id}"

    conn.close()
    print(msg)
    return msg

# ================= SCAN QR =================
def scan_qr():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    scanned_ids = set()

    if not cap.isOpened():
        print("❌ Cannot access webcam")
        return

    print(f"📅 Attendance Date: {today}")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)

        if data:
            student_id = data.strip()
            if student_id not in scanned_ids:
                mark_present(student_id)
                scanned_ids.add(student_id)

            cv2.putText(frame, f"ID: {student_id}",
                        (40, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 2)

        cv2.imshow("QR Attendance System", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("🛑 Scanning stopped")

# ================= RUN =================
init_today_attendance()
scan_qr()

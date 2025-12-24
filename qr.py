# generate_qr.py
import qrcode

# Ask user for student ID
student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")

# Create QR code
qr_data = str(student_id)  # the QR code will contain only the ID
img = qrcode.make(qr_data)

# Save QR code with name
filename = f"{student_name}_{student_id}.png"
img.save(filename)

print(f"✅ QR code created for {student_name} with ID {student_id} as {filename}")

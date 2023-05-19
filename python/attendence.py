# Attendance App

import csv

def mark_attendance(student_id):
    with open('attendance.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([student_id, 'Present'])

def view_attendance():
    with open('attendance.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0], row[1])

while True:
    print('1. Mark Attendance')
    print('2. View Attendance')
    print('3. Exit')
    choice = input('Enter your choice: ')
    
    if choice == '1':
        student_id = input('Enter student ID: ')
        mark_attendance(student_id)
        print('Attendance marked successfully!')
        
    elif choice == '2':
        view_attendance()
        
    elif choice == '3':
        break
        
    else:
        print('Invalid choice. Please try again.')

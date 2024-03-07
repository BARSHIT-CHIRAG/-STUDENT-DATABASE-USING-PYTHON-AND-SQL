import sqlite3
 # Create a connection to the database
conn = sqlite3.connect('student.db')
cursor = conn.cursor()
 # Create the student table if it doesn't exist
cursor.execute('''
 CREATE TABLE IF NOT EXISTSstudents (
 roll_noINTEGER PRIMARYKEY,
 name TEXT,
 ageINTEGER,
 branchTEXT,
 cgpa FLOAT
 )
 ''')
 # Functiontoadda newstudent to the database
def add_student(roll_no, name, age,branch, cgpa):
 cursor.execute('INSERTINTO students (roll_no, name,age, branch,cgpa)','VALUES(?,?,?, ?, ?)','(roll_no, name, age,branch, cgpa)')
 conn.commit()
 print("Student added successfully.")
 # Functiontoretrieve allstudent data from the database
 def get_students():
     cursor.execute('SELECT* FROM students')
 rows= cursor.fetchall()
 if len(rows)== 0:
     print("Nostudents found.")
 else:
     for row in rows:
         print(f"RollNo: {row[0]}, Name: {row[1]}, Age: {row[2]},
 Branch: {row[3]}, CGPA: {row[4]}")
 # Functiontosearchfor astudent by roll number
 def search_student(roll_no):
    cursor.execute('SELECT* FROM studentsWHERE roll_no= ?', (roll_no,))
 row= cursor.fetchone()
 if row is None:
     print("Student Not Found.")
 else:
     print(f"RollNo: {row[0]}, Name: {row[1]}, Age: {row[2]}, Branch:
 {row[3]}, CGPA: {row[4]}")
 # Mainprogram
 while True:
  print("\n1. Adda Student")
 print("2. GetAll Students")
 print("3. SearchFor aStudent ByRoll Number")
 print("4. Quit")
 choice = input("EnterYour Choice (1-4): ")
 if choice == '1':
  roll_no= int(input("EnterStudent Roll Number:"))
 name = input("EnterStudent Name:")
 age= int(input("EnterStudent Age: "))
 branch= input("EnterStudent Branch: ")
 cgpa = float(input("EnterStudent CGPA:"))
 add_student(roll_no, name,age, branch,cgpa)
 elif choice== '2':
 get_students()
 elif choice== '3':
 roll_no = int(input("Enter Student Roll Number: "))
 search_student(roll_no)
 elif choice == '4':
 break
 else:
 print("Invalid choice. Please try again.")
 # Close the database connection
 conn.close()
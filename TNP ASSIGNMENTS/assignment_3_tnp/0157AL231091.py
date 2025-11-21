#Name - Himang Sahu
#Enrollment Number - 0157AL231091
#Batch - 5
#Batch Timing -10.30 to 12.10


import random
from datetime import datetime

class StudentProfile:
    # Class to handle student user data and file operations
    def __init__(self, enrollment="", name="", email="", branch="", year="", phone_no="", secret_key=""): # Changed: email_id
        self.enrollment = enrollment
        self.name = name
        self.email = email # Changed: email_id
        self.branch = branch
        self.year = year
        self.phone_no = phone_no
        self.secret_key = secret_key # Stores the password

    def save_data(self):
        # Appends student data to the file
        with open("students_data.txt", "a") as f:
            f.write(f"{self.enrollment},{self.name},{self.email},{self.branch},{self.year},{self.phone_no},{self.secret_key}\n") # Changed variable

    @staticmethod
    def load_profiles():
        # Loads all student data from the file into a dictionary (key: enrollment)
        student_profiles = {}
        try:
            with open("students_data.txt", "r") as f:
                for line in f:
                    e, n, em, b, y, c, p = line.strip().split(",")
                    student_profiles[e] = StudentProfile(e, n, em, b, y, c, p)
        except FileNotFoundError:
            pass
        return student_profiles
    
    @staticmethod
    def update_profile_data(modified_profile):
        # Rewrites the entire file with updated user data
        student_profiles = StudentProfile.load_profiles()
        student_profiles[modified_profile.enrollment] = modified_profile
        with open("students_data.txt", "w") as f:
            for s in student_profiles.values():
                f.write(f"{s.enrollment},{s.name},{s.email},{s.branch},{s.year},{s.phone_no},{s.secret_key}\n") # Changed variable


class Quiz:
    # Holds all quiz questions categorized by topic
    questions = {
        "DSA": [
            ("Which data structure uses FIFO?", ["Stack", "Queue", "Tree", "Graph"], "Queue"),
            ("Python uses which data structure for recursion?", ["Queue", "Stack", "Heap", "List"], "Stack"),
            ("Best case time complexity of Binary Search?", ["O(n)", "O(log n)", "O(n2)", "O(1)"], "O(log n)"),
            ("Which sorting is stable?", ["Quick", "Merge", "Heap", "Selection"], "Merge"),
            ("Which is non-linear DS?", ["Array", "Queue", "Tree", "Stack"], "Tree")
        ],
        "DBMS": [
            ("What is SQL?", ["Programming language", "Query language", "OS", "Compiler"], "Query language"),
            ("DBMS stands for?", ["Data Base Model System", "Database Management System", "Data Manage System", "None"], "Database Management System"),
            ("Primary key is?", ["Unique & Not NULL", "NULL allowed", "Duplicate allowed", "None"], "Unique & Not NULL"),
            ("Which joins tables?", ["JOIN", "SELECT", "DELETE", "UPDATE"], "JOIN"),
            ("Normalization reduces?", ["Redundancy", "Speed", "Size", "Security"], "Redundancy")
        ],
        "PYTHON": [
            ("Python is?", ["Low level", "High level", "Machine language", "None"], "High level"),
            ("Which keyword defines a function?", ["func", "define", "def", "fun"], "def"),
            ("List is?", ["Mutable", "Immutable", "Constant", "None"], "Mutable"),
            ("Which operator for power?", ["^", "**", "%", "//"], "**"),
            ("Dictionaries store?", ["Ordered pairs", "Key-value pairs", "Characters", "Loops"], "Key-value pairs")
        ]
    }

    @staticmethod
    def start_quiz(current_user):
        # Runs a 5-question quiz for the selected category
        print("Choose Category:")
        print("1. DSA")
        print("2. DBMS")
        print("3. PYTHON")
        user_choice = input("Enter choice: ")

        category = { "1":"DSA", "2":"DBMS", "3":"PYTHON" }.get(user_choice)
        if not category:
            print("Invalid category")
            return
        
        quiz_qs = Quiz.questions[category]
        random.shuffle(quiz_qs) # Randomizes question order
        current_score = 0

        for question_text, options, correct_answer in quiz_qs[:5]: # Takes the first 5 questions
            print(f"{question_text}")
            for index, option in enumerate(options, 1):
                print(f"{index}. {option}")
            student_answer = input("Your answer: ")

            # Validates and checks the user's answer against the correct answer
            if student_answer.isdigit():
                try:
                    ans_index = int(student_answer) - 1
                    if 0 <= ans_index < len(options) and options[ans_index] == correct_answer:
                        current_score += 1
                except IndexError:
                    pass

        total_questions = 5
        print(f"Score: {current_score}/{total_questions}")

        # Logs the quiz result to a file
        with open("quiz_results.txt","a") as f:
            f.write(f"{current_user.enrollment},{category},{current_score}/{total_questions},{datetime.now()}\n")


class System:
    # Main application handler
    def __init__(self):
        self.active_student = None # Stores the currently logged-in student object

    def register_student(self):
        # Registers a new student and saves their data
        print("Student Registration ")
        e = input("Enrollment: ")
        student_profiles = StudentProfile.load_profiles()
        if e in student_profiles:
            print("User already exists!")
            return

        n = input("Name: ")
        em = input("Email: ")
        b = input("Branch: ")
        y = input("Year: ")
        c = input("Phone No: ")
        p = input("Password: ")

        new_student = StudentProfile(e,n,em,b,y,c,p)
        new_student.save_data()
        print("Registration successful!")

    def user_login(self):
        # Authenticates user and sets the active_student object upon success
        print("User Login")
        e = input("Enrollment: ")
        p = input("Password: ")

        student_profiles = StudentProfile.load_profiles()
        if e in student_profiles and student_profiles[e].secret_key == p:
            self.active_student = student_profiles[e]
            print("Login successful!")
        else:
            print("Invalid credentials")

    def update_student_profile(self):
        # Allows the active student to modify their profile details
        if not self.active_student:
            print("Login first")
            return
        print("Update details")
        # Update attributes, keeping old value if input is blank
        self.active_student.name = input(f"Name ({self.active_student.name}): ") or self.active_student.name
        self.active_student.email = input(f"Email ({self.active_student.email}): ") or self.active_student.email # Changed variable
        self.active_student.branch = input(f"Branch ({self.active_student.branch}): ") or self.active_student.branch
        self.active_student.year = input(f"Year ({self.active_student.year}): ") or self.active_student.year
        self.active_student.phone_no = input(f"Phone No ({self.active_student.phone_no}): ") or self.active_student.phone_no
        
        new_password = input(f"Password: ")
        self.active_student.secret_key = new_password or self.active_student.secret_key

        StudentProfile.update_profile_data(self.active_student)
        print("Profile Updated!")

    def view_profile(self):
        # Displays the current student's profile information
        if not self.active_student:
            print("Login first")
            return
        s = self.active_student
        print("Student Profile")
        print(f"Enrollment: {s.enrollment}")
        print(f"Name: {s.name}")
        print(f"Email: {s.email}") # Changed variable
        print(f"Branch: {s.branch}")
        print(f"Year: {s.year}")
        print(f"Phone No: {s.phone_no}")

    def user_logout(self):
        # Clears the active student session
        self.active_student = None
        print("Logged Out")

    def execute_system(self):
        # Main loop for the application menu
        while True:
            print("STUDENT SYSTEM")
            print("1 Register Student")
            print("2 User Login")
            print("3 View Profile")
            print("4 Update Profile")
            print("5 Start Quiz")
            print("6 User Logout")
            print("7 Exit System")
            
            ch = input("Enter choice: ")

            if ch=="1": self.register_student()
            elif ch=="2": self.user_login()
            elif ch=="3": self.view_profile()
            elif ch=="4": self.update_student_profile()
            elif ch=="5":
                if self.active_student:
                    Quiz.start_quiz(self.active_student)
                else:
                    print("Login first")
            elif ch=="6": self.user_logout()
            elif ch=="7": break
            else: print("Invalid choice")


System().execute_system()
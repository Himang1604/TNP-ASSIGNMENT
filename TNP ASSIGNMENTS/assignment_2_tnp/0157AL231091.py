# global variables to track the logged in users

logged_in_user = ""
is_logged_in = False
student_file = "students.txt"

#  functions for each menu option

def register_student():
#  adds a new student with 10 fields to our text file
    print(" new student registration \n")
    
    username = input("create a username: ")
    
    # check if the username is already taken by reading the file
    try:
        with open(student_file, "r") as file:
            for line in file:
                stored_username = line.strip().split(",")[0]
                if stored_username == username:
                    print("this username already exists so please try another")
                    return
    except FileNotFoundError:
        pass
    
    password = input("Create a password: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    dob = input("Enter your Date of Birth (DD-MM-YYYY): ")
    course = input("Enter your course : ")
    year = input("Enter your enrollment year: ")
    address = input("Enter your address: ")
    
    with open(student_file, "a") as file:
        # we join all 10 pieces of data with commas and add a newline character
        file.write(f"{username},{password},{first_name},{last_name},{email},{phone},{dob},{course},{year},{address}\n")
        
    print("\n registration successful, you can now log in")

def login():
#   logs a student in by checking their credentials against the file
    global is_logged_in, logged_in_user
    print(" Student Login \n")
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        with open(student_file, "r") as file:
            for line in file:
                
                user_data = line.strip().split(",")
                stored_username = user_data[0]
                stored_password = user_data[1]
                
                if stored_username == username and stored_password == password:
                    is_logged_in = True
                    logged_in_user = username
                    print(f"\n welcome {user_data[2]}, you are now logged in ")
                    return
    except FileNotFoundError:
        print("no students have been registered yet")
        return
        
    print("\n wrong username or password")

def show_profile():
#   finds and displays the details for the currently logged in user
    if not is_logged_in:
        print("you need to be logged in to see your profile ")
        return
        
    print("your profile \n")
    with open(student_file, "r") as file:
        for line in file:
            user_data = line.strip().split(",")
            
            if user_data[0] == logged_in_user:
                print(f"Username: {user_data[0]}")
                print(f"First Name: {user_data[2]}")
                print(f"Last Name: {user_data[3]}")
                print(f"Email: {user_data[4]}")
                print(f"Phone: {user_data[5]}")
                print(f"Date of Birth: {user_data[6]}")
                print(f"Course: {user_data[7]}")
                print(f"Enrollment Year: {user_data[8]}")
                print(f"Address: {user_data[9]}")
                return

# allows a user to update their profile info
def update_profile():
    if not is_logged_in:
        print("you need to be logged in to update your profile")
        return
    
    print(" update your profile \n")
    all_lines = []
    user_found = False

    try:
        with open(student_file, "r") as file:
            all_lines = file.readlines()
    except FileNotFoundError:
        print("error , could not find student file")
        return

    for i in range(len(all_lines)):
        user_data = all_lines[i].strip().split(',')
        if user_data[0] == logged_in_user:
            user_found = True
            print("which detail would you like to update?")
            print("1. Phone Number")
            print("2. Address")
            choice = input("Enter your choice: ")

            if choice == '1':
                new_phone = input("Enter new phone number: ")
                user_data[5] = new_phone
            elif choice == '2':
                new_address = input("Enter new address: ")
                user_data[9] = new_address
            else:
                print("wrong choice.")
                return

            all_lines[i] = ",".join(user_data) + "\n"
            print("\n profile updated successfully")
            break
    
    if user_found:
        with open(student_file, "w") as file:
            file.writelines(all_lines)

def logout():
#  logs the current user out
    global is_logged_in, logged_in_user
    if not is_logged_in:
        print(" you are not currently logged in ")
        return
        
    print(f" bye {logged_in_user}, you have been logged out")
    is_logged_in = False
    logged_in_user = ""

# main Program

def main():
#   the main menu that the user interacts with
    while True:
        print("\n welcome to the simple student page ")
        if is_logged_in:
            print(f"(logged in as: {logged_in_user})")
            choice = input("""
            choose an option:
            1. show Profile
            2. Update Profile
            3. logout
            4. exit
            
            enter choice (1-4): """)
            
            if choice == "1":
                show_profile()
            elif choice == "2":
                update_profile()
            elif choice == "3":
                logout()
            elif choice == "4":
                print("exiting program.")
                break
            else:
                print(" wrong choice, please try again.")
        else:
            choice = input("""
            choose an option:
            1. register
            2. login
            3. exit
            
            enter choice (1-3): """)

            if choice == "1":
                register_student()
            elif choice == "2":
                login()
            elif choice == "3":
                print("exiting program.")
                break
            else:
                print("wrong choice, please try again.")
        
        
        input("\n press enter to continue")


main()
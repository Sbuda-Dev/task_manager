#=====importing libraries===========

import datetime

with open("user.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
       pass
         
    user_enter = input("Please enter username: ")
    user_password = input("Please enter your password: ")

while user_enter not in line or user_password not in line:

        print("Incorrect username or password. Please enter correct username and password.")
        user_enter = input("Please enter username: ")
        user_password = input("Please enter your password: ")

if user_enter == 'admin' and user_password in line:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
     menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - statistics
e - exit
: ''').lower()

if user_enter != 'admin' and user_password in line:
     menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
      
if menu == 'r' and user_enter == 'admin':
    with open("user.txt", "a") as f:
        new_username = input("Create your username: ")
        new_userpass = input("Create your password: ")
        confirm_pass = input("Please confirm password: ")
        if new_userpass == confirm_pass:
            f.write(", ")
            f.write(new_username)
            f.write(", ")
            f.write(new_userpass)
        else:
            while new_userpass != confirm_pass:
                print("Passwords do not match. Please try again.")
                new_userpass = input("Create your password: ")
                confirm_pass = input("Please confirm password: ")

elif menu == 'a':
        with open("tasks.txt", "a") as f:

            user = input("Enter username: ")
            f.write("\n")
            f.write(user)
            f.write(",")
            title = input("Enter the title of the task: ")
            f.write(title)
            f.write(",")
            descrip = input("Enter description of the task: ")
            f.write(descrip)
            f.write(",")
            due_date = input("Enter date when task is due(day month year): ")
            f.write(due_date)
            f.write(",")
            current_date = datetime.datetime.now().date()
            f.write(str(current_date))
            f.write(",")
            completed = 'No'
            f.write(completed)
        
elif menu == 'va':
        with open("tasks.txt", "r") as f:

            lines = f.readlines()    
            for line in lines:
                temp = line.strip()
                temp = temp.split()
                first_line = " ".join(temp)
                username, title, descrip, date_assigned, due_date, completed = first_line.split(",")

                print("Title: ",title)
                print("Assigned to: ",username)
                print("Date assigned: ",date_assigned)
                print("Due date: ",due_date)
                print("Task complete? ",completed)
                print("Task description: ",descrip)
        
elif menu == 'vm':
        with open("tasks.txt", "r") as f:

            lines = f.readlines()
            for line in lines:
                temp = line.strip()
                temp = temp.split()
                first_line = " ".join(temp)
                username, title, descrip, date_assigned, due_date, completed = first_line.split(",")
                    
                if username == user_enter:                    
                    print("Title: ",title)
                    print("Assigned to: ",username)
                    print("Date assigned: ",date_assigned)
                    print("Due date: ",due_date)
                    print("Task complete? ",completed)
                    print("Task description: ",descrip)
                else:
                    print("Logged on username is not the same.")
        
elif menu == 's':
            with open("tasks.txt", "r") as task:
                with open("user.txt", "r") as user:
                         
                    task_line = task.readlines()
                    print("Number of tasks: ",len(task_line))

                    users = user.readlines()
                    for line in users:
                            temp = line.strip()
                            temp = temp.split()
                            temp_length = len(temp)

                    count_users = temp_length / 2                             
                    print("Number of user/s: ",int(count_users)) 
                                       
elif menu == 'e':
    print('Goodbye!!!')
    exit()

else:
    print("Invalid input")

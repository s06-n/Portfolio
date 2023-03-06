#=====importing libraries===========

import datetime

#====Login Section====
'''This code reads usernames and passwords from a text file which are stored in a dictionary.
   Then usernames and passwords are validated.'''
user_login_dict = {}
user_tasks_read = []
user_logins = open("user.txt", "r+", encoding="utf-8")

user_logins.seek(0)
user_login_details = user_logins.readlines()

for line in user_login_details:
    line = line.replace("\n", "")
    (key, val) = line.split(", ")    # Usernames and passwords are separated by a comma,
    user_login_dict[key] = val       # which is used to store them in a dictionary.

while True:
    username = input("Please input your username: ").lower()
    password = input("Please input your password: ").lower()
    if username in user_login_dict and password == user_login_dict.get(username):
        print("Welcome back!")
        break
    else:
        print("Your login details are incorrect, please try again.")
        continue
user_logins.close()

#====Menu Options====

while True:
    if username == "admin":
        menu = input('''Select one of the following options below:
    r  - Registering a user
    a  - Adding a task
    va - View all tasks
    vm - View my task
    ds - Display statistics
    gr - Generate reports
    e  - Exit
    : ''').lower()
    else:
        menu = input('''Select one of the following options below:
    r  - Registering a user
    a  - Adding a task
    va - View all tasks
    vm - View my task
    e  - Exit
    : ''').lower()

#Registering a user.
#Only the user admin can register users.
    if menu == 'r':
        pass

        if username != "admin":
            print("You do not have the permissions to register users.\n")
            continue
        else:
            print("You have permission to register users.\n")

        def reg_user():
            user_logins = open("user.txt", "a+", encoding="utf-8")
            while True:
                new_user_name = input("Please enter a new username: ").lower()
                if new_user_name in user_login_dict:  # This makes sure there are no duplicate usernames stored.
                    print("That username already exists, please try again.")
                else:
                    new_password = input("Please enter a new password: ").lower()
                    new_password_confirmation = input("Please confirm your password: ").lower()
                    if new_password == new_password_confirmation:
                        user_logins.write(f"\n{new_user_name}, {new_password}")
                        break
                    else:
                        print("Your password does not match, please try again.")

            user_logins.close()
        reg_user()
#Adding a new task.
    elif menu == 'a':
        pass

        def add_task():
            user_tasks = open("tasks.txt", "a+", encoding="utf-8")
            username_task = input("Please type the username of the user who is assigned the task: ")
            title_task = input("Please type the title of the task: ")
            description = input("Please type a description of the task: ")
            due_date_task = input("Please type the due date of the task (e.g. 01 Jan 2023):  ")
            now = datetime.datetime.now()
            current_date = now.strftime("%d %b %Y")
            assigned_date_task = current_date
            task_complete = "No"
            user_task_input = f"\n{username_task}, {title_task}, {description}, {due_date_task}, " \
                              f"{assigned_date_task}, {task_complete}"
            user_tasks.write(user_task_input)
            user_tasks.close()
        add_task()
#Viewing all tasks.
    elif menu == 'va':
        pass

        def view_all():
            user_tasks = open("tasks.txt", "r+", encoding="utf-8")
            user_tasks_read = user_tasks.readlines()
            user_tasks.close()
            for line in user_tasks_read:
                split_data = line.split(", ")
                output = "――――――――――――――――――――――――――――――――――\n"
                output += "\n"
                output += f"Assigned to:        {split_data[0]}\n"
                output += f"Task:               {split_data[1]}\n"
                output += f"Task Description:   {split_data[2]}\n"
                output += f"Due Date:           {split_data[3]}\n"
                output += f"Assigned Date:      {split_data[4]}\n"
                output += f"Task Completed:     {split_data[5]}\n"
                output += "\n"
                output += "――――――――――――――――――――――――――――――――――\n"
                print(output)
        view_all()


#Viewing only the user's task.
#If the user has no tasks, a sentence is printed.
    elif menu == 'vm':
        pass

        def view_mine():
            count = 0
            user_tasks = open("tasks.txt", "r", encoding="utf-8")
            user_tasks_read = user_tasks.readlines()
            for pos, line in enumerate(user_tasks_read, 1):
                if username in line:
                    count += 1
                    split_data = line.strip("\n").split(", ")
                    output = f"―――――――――――――――――――――――――[{pos}]――――――――――――――――――――――――――\n"
                    output += "\n"
                    output += f"Assigned to:        {split_data[0]}\n"
                    output += f"Task:               {split_data[1]}\n"
                    output += f"Task Description:   {split_data[2]}\n"
                    output += f"Due Date:           {split_data[3]}\n"
                    output += f"Current Date:       {split_data[4]}\n"
                    output += f"Task Completed:     {split_data[5]}\n"
                    output += "\n"
                    output += "―――――――――――――――――――――――――――――――――――――――――――――――――――――\n"
                    print(output)
                if count == 0:
                    print("There are no tasks.")
            #This code will allow users to edit tasks.
            while True:
                task_number = int(input("Please enter the task number or -1 to exit: "))
                if task_number == -1:
                    print("You are now exiting")
                    break

                if task_number == 0 or task_number < -1 or task_number > len(user_tasks_read):
                    print("You have selected an invalid option, please try again.")
                    continue

                edit_task = user_tasks_read[task_number - 1]

                while True:
                    output = f"―――――――――――――――――――――――――[SELECT AN OPTION]――――――――――――――――" \
                             f"――――――――――\n"
                    output += "1 - edit the task\n"
                    output += "2 - mark the task as complete\n"
                    output += "―――――――――――――――――――――――――――――――――――――――――――――――――――――\n"

                    choice = int(input(output))
                    if choice <= 0 or choice >= 3:
                        print("You have selected an invalid option, please try again.")

                    if choice == 1:
                        edit_choice = input("Please choose from the following:\n"
                                            "u - edit username\n"
                                            "d - edit due date\n"
                                            ": ").lower()

                        if edit_choice == "u":
                            split_data = edit_task.strip("\n").split(", ")
                        while True:
                            if split_data[-1] == "No":
                                split_data[0] = input("Please enter a valid username: ")
                                if split_data[0] in user_login_dict:
                                    new_data = ", ".join(split_data)
                                    user_tasks_read[task_number - 1] = f"{new_data}\n"
                                    break
                                else:
                                    print("That is not a valid username, please try again.")
                                    continue
                            else:
                                print("You cannot edit this task.")

                        if edit_choice == "d":
                            split_data = edit_task.split(", ")

                            if split_data[-1] == "No":
                                split_data[-3] = input("Please enter a valid date e.g. 01 Feb 2023: ")
                                new_data = ", ".join(split_data)
                                user_tasks_read[task_number - 1] = new_data
                            else:
                                print("You cannot edit this task.")

                    elif choice == 2:
                        split_data = edit_task.split(", ")
                        split_data[-1] = "Yes"
                        new_data = ", ".join(split_data)
                        user_tasks_read[task_number - 1] = new_data
                    user_tasks_write = open("tasks.txt", "w+", encoding="utf-8")
                    for line in user_tasks_read:
                        user_tasks_write.write(line)

                    user_tasks_write.close()
                    break
            user_tasks.close()
        view_mine()

#Statistics: showing the total number of users and tasks.
#Only the user admin can see statistics.
    elif menu == 'ds':
        if username != "admin":
            print("You have made a wrong choice. Please try again.\n")
            continue
        else:
            print("You have permission to see the statistics.\n")

        def display_stats():
            user_logins = open("user.txt", "r", encoding="utf-8")
            user_tasks = open("tasks.txt", "r", encoding="utf-8")
            user_logins_r = user_logins.readlines()
            user_tasks_r = user_tasks.readlines()
            print("――――――――――――――Statistics―――――――――――――――――\n")
            print(f"There are a total of {len(user_tasks_r)} tasks.\n")
            print(f"There are a total of {len(user_logins_r)} users.\n")
            print("―――――――――――――――――――――――――――――――――――――\n")
            user_logins.close()
            user_tasks.close()
        display_stats()
# Reports: showing two reports about the tasks and users.
# Only the user admin can see the reports.
    elif menu == 'gr':
        if username != "admin":
            print("You have made a wrong choice. Please try again.\n")
            continue
        else:
            print("You have permission to see the reports.\n")

        def gen_reports():
            # This code will generate report files and write data to them.
            task_report = open("task_overview.txt", "w+", encoding="utf-8")
            user_report = open("user_overview.txt", "w+", encoding="utf-8")

            user_tasks = open("tasks.txt", "r+", encoding="utf-8")
            user_tasks_read = user_tasks.readlines()

            user_tasks.close()

            count_completed = 0
            count_incomplete = 0
            overdue_tasks = 0
            count_incomplete_overdue = 0
            now = datetime.datetime.now()
            current_date = now.strftime("%d %b %Y")
            total_tasks = len(user_tasks_read)
            # This code checks the tasks to calculate figures for the report e.g. task completed, overdue etc.
            for line in user_tasks_read:
                tasks = line.strip("\n").split(", ")
                completed = tasks[-1]
                due_date_check = tasks[-3]

                if due_date_check < current_date:
                    overdue_tasks += 1

                if completed == "Yes":
                    count_completed += 1
                else:
                    count_incomplete += 1

                if due_date_check < current_date and completed == "No":
                    count_incomplete_overdue += 1

            task_report.write(f"Total tasks: {total_tasks}.\n")
            task_report.write(f"Total completed tasks: {count_completed}.\n")
            task_report.write(f"Total incomplete tasks: {count_incomplete}.\n")
            task_report.write(f"Total incomplete and overdue tasks: {count_incomplete_overdue}.\n")
            task_report.write(f"Percent incomplete tasks: {round((count_incomplete/total_tasks)*100)}%.\n")
            task_report.write(f"Total overdue tasks: {overdue_tasks}.\n")
            task_report.write(f"Percent overdue tasks: {round((overdue_tasks/total_tasks)*100)}%.\n")

            given_user = []
            tasks_complete = 0
            tasks_incomplete = 0
            tasks_overdue = 0
            tasks_assigned = 0
            tasks_incomplete_overdue = 0
            tasks = []

            user_report.write(f"Total users: {len(user_login_dict)}.\n")
            user_report.write(f"Total tasks: {total_tasks}.\n")

            for line in user_tasks_read:
                word = line.strip("\n").split(", ")
                tasks += [word]

            for users in user_login_dict:
                for row in range(len(tasks)):
                    if users == tasks[row][0]:
                        given_user.append(users)
                        tasks_assigned += 1

                        if tasks[row][-1] == "Yes":
                            tasks_complete += 1
                        else:
                            tasks_incomplete += 1

                        if tasks[row][-3] < current_date:
                            tasks_overdue += 1

                        if tasks[row][-1] == "No" and tasks[row][-3] < current_date:
                            tasks_incomplete_overdue += 1
                    else:
                        continue

                if total_tasks == 0:
                    percent_tasks = 0
                else:
                    percent_tasks = round((tasks_assigned/total_tasks)*100, 2)

                if tasks_assigned == 0:
                    percent_complete = 0
                    percent_incomplete = 0
                    percent_overdue = 0
                    percent_incomplete_overdue = 0
                else:
                    percent_complete = round((tasks_complete/tasks_assigned)*100, 2)
                    percent_incomplete = round((tasks_incomplete/tasks_assigned)*100, 2)
                    percent_overdue = round((tasks_overdue/tasks_assigned)*100, 2)
                    percent_incomplete_overdue = round((tasks_incomplete_overdue/tasks_assigned)*100, 2)

                if not given_user:
                    continue
                user_report.write(str(f"User: {given_user[0]}") + ", "+str(f"Percentage of tasks: {percent_tasks}%") +
                                  ", " + str(f"Percent complete: {percent_complete}%") + ", " +
                                  str(f"Percent incomplete: {percent_incomplete}%") + ", " +
                                  str(f"Percent overdue: {percent_overdue}%") + ", " +
                                  str(f"Percent incomplete and overdue: {percent_incomplete_overdue}%" + "\n"))

                given_user = []
                tasks_complete = 0
                tasks_incomplete = 0
                tasks_overdue = 0
                tasks_assigned = 0
                tasks_incomplete_overdue = 0

            print("The reports have been generated!")
            task_report.close()
            user_report.close()

            task_report = open("task_overview.txt", "r", encoding="utf-8")
            user_report = open("user_overview.txt", "r", encoding="utf-8")
            task_report_read = task_report.readlines()
            user_report_read = user_report.readlines()

            print("------------------------TASK OVERVIEW----------------------------")
            print("―――――――――――――――――――――――――――――――――――――――――\n")
            for line in task_report_read:
                print(line)
            print("―――――――――――――――――――――――――――――――――――――――――\n")

            print("------------------------USER OVERVIEW----------------------------")
            print("―――――――――――――――――――――――――――――――――――――――――\n")
            for line in user_report_read:
                line = line.replace(", ", "\n")
                print(line)
                print("―――――――――――――――――――――――――――――――――――――――――\n")
            print("------------------------------------------------------------------")
            task_report.close()
            user_report.close()
        gen_reports()
#Exits the program.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

#If the user does not write a letter in the menu, they are prompted to try again.
    else:
        print("You have made a wrong choice. Please try again.")
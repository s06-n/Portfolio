"""This program will simulate a calculator."""


def calculator():
    lines = ""
#--This code starts with the opening of a file and for the user to pick from a menu with error handling.---
    while True:
        file = open("calculator.txt", "a+", encoding="utf-8")
        try:
            user_choice = int(input("Please choose from the following options:\n"
                            "1 - to print previous calculations.\n"
                            "2 - to use the calculator.\n"
                            "3 - to exit.\n"
                            ": "))

        except Exception:
            print("That was not a valid choice, please try again.")
            continue

        while True:
            if user_choice == 1:  # This choice prints a list of previous calculations from a text file.
                file_name = input("Please enter the file name: ")
                if file_name != "calculator":
                    print("That file name does not exist, please try again.")
                else:
                    file.seek(0)
                    file_read = file.readlines()
                    print(file_read)
                    for line in file_read:
                        lines += line
                    print(f"The calculations are: \n{lines}")
                    break

            elif user_choice == 2:  # This choice will allow for the user to use the calculator and write to the file.
                print("---To use the calculator, you will be prompted to enter two numbers and "
                      "to choose an operation---")
                while True:
                    try:
                        number_one = int(input("Please enter a number: "))
                        number_two = int(input("Please enter another number: "))
                        break
                    except Exception:
                        print("That was not a valid number, please try again.")
                while True:
                    operation = input("Please choose an operation from the list:\n"
                                      "m = multiplication\n"
                                      "d = division\n"
                                      "a = addition\n"
                                      "s = subtraction\n"
                                      ": ").lower()

                    if operation == "m":  # Multiplication
                        calculation = round((number_one * number_two), 2)
                        print(f"{number_one} * {number_two} = {calculation}")
                        file.write(f"{number_one} * {number_two} = {calculation}\n")
                        break

                    elif operation == "d":  # Division.
                        if number_two == 0:  # in case the user divides by 0.
                            print("Whoa you cannot divide by zero!")
                            print(f"{number_one} / {number_two} = undefined")
                            file.write(f"{number_one} / {number_two} = undefined\n")
                            break
                        else:
                            calculation = round((number_one / number_two), 2)
                            print(f"{number_one} / {number_two} = {calculation}")
                            file.write(f"{number_one} / {number_two} = {calculation}\n")
                            break

                    elif operation == "a":  # Addition.
                        calculation = round((number_one + number_two), 2)
                        print(f"{number_one} + {number_two} = {calculation}")
                        file.write(f"{number_one} + {number_two} = {calculation}\n")
                        break

                    elif operation == "s":  # Subtraction.
                        calculation = round((number_one - number_two), 2)
                        print(f"{number_one} - {number_two} = {calculation}")
                        file.write(f"{number_one} - {number_two} = {calculation}\n")
                        break
                    else:
                        print("You have made the wrong choice, please try again!")
                break

            elif user_choice == 3:  # To exit.
                print("You have now exited.")
                exit()
            else:
                print("That was not a valid choice, please try again.")

        file.close()


calculator()
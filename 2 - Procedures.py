def problem1():
    def task1():
        print("This is task 1!")

    def task2():
        print("This is task 2!")

    def task3():
        print("This is task 3!")

    task1()
    task2()
    task3()

def problem2():
    def askName():
        name = input("What is your name? ")

    def askAge():
        age = int(input("What is your age? "))

    choice = input("Would you like to teach me your name or age? Enter 1 for name, and 2 for age: ")
    if choice == "1":
        askName()
        print("Your name is " + name)
    elif choice == "2":
        askAge()





def main():
    while True:
        print("Choose a problem to run.")
        choice = input("Enter your choice: ")

        if choice == "1":
            problem1()
        elif choice == "2":
            problem2()
        elif choice == "3":
            problem3()
        elif choice == "4":
            problem4()
        elif choice == "5":
            problem5()
        else:
            print ("This is not a valid choice. Please select a number from 1-10")

if __name__ == "__main__":
                main()























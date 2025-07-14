# Task 1 - Output the text "Hello world!" on the screen.
def problem1():
    print("Hello world!")

# Task 2 - Ask a user for their name, store the result in a variable, say "hello" to them
def problem2():
    task2_name = input("What is your name? ")
    print("Hello " + task2_name)

def problem3():
    task3_name = input("What is your name? ")
    task3_favouritecolour = input("What is your favourite colour? ")
    print("OK " + task3_name + ", you like the colour " + task3_favouritecolour + ".")

def problem4():
    task4_number = float(input("Please enter a number: "))
    task4_half = task4_number / 2
    print("Half of your number is " + str(task4_half) + "!")

def problem5():
    task5_score = int(input("Please enter a score: "))
    task5_maximumScore = int(input("Please enter a maximum score: "))
    task5_percentage = task5_score / task5_maximumScore * 100
    print("Your score is " + str(task5_percentage) + "%")


# Task picker
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


if __name__ == "__main__":
                main()

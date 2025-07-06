# Task 1 - Output the text "Hello world!" on the screen.
def problem1():
    print("Hello world!")

# Task 2 - Ask a user for their name, store the result in a variable, say "hello" to them
def problem2():
    task2_name = input("What is your name? ")
    print("Hello " + task2_name)





# Task picker
def main():
    while True:
        print("Choose a problem to run.")
        choice = input("Enter your choice: ")

        if choice == "1":
            problem1()
        elif choice == "2":
            problem2()


if __name__ == "__main__":
                main()

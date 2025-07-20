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

def problem6():
    task6_num1 = int(input("Please enter your first number: "))
    task6_num2 = int(input("Please enter your second number: "))
    task6_num3 = int(input("Please enter your third number: "))
    task6_total = task6_num1 + task6_num2 + task6_num3
    print(task6_total)

def problem7():
    task7_input = input("Please enter a phrase: ")
    print(task7_input, task7_input, task7_input)

def problem8():
    task8_num1 = int(input("Enter your first number: "))
    task8_num2 = int(input("Enter your second number: "))
    task8_percentage = task8_num1 / task8_num2 * 100
    print(str(task8_num1) + " is " + str(task8_percentage) + "% of " + str(task8_num2))

def problem9():
    task9_item1 = input("Enter your first item that you would like to purchase: ")
    task9_price1 = float(input("Enter the cost of the item in GBP: "))
    task9_item2 = input("Enter your second item that you would like to purchase: ")
    task9_price2 = float(input("Enter the cost of the item in GBP: "))
    task9_totalPrice = task9_price1 + task9_price2
    print(task9_item1 + " and " + task9_item2 + " will cost £" + str(task9_totalPrice))

def problem10():
    task10_name = input("Please enter your name: ")
    task10_age = int(input("Please enter your age: "))
    task10_height = float(input("Please enter your height in centimetres: "))
    task10_newHeight = task10_height * 1.05
    task10_newAge = task10_age + 1
    print("When " + task10_name + " is " + str(task10_newAge) + " years old, he will be approximately " + str(task10_newHeight) + " centimetres tall.")

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
        elif choice == "6":
            problem6()
        elif choice == "7":
            problem7()
        elif choice == "8":
            problem8()
        elif choice == "9":
            problem9()
        elif choice == "10":
            problem10()
        else:
            print ("This is not a valid choice. Please select a number from 1-10")


if __name__ == "__main__":
                main()

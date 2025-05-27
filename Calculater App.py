# My name is Yohan Shanuka

def addition (num1, num2):
    return num1 + num2

def subtraction (num1, num2):
    return num1 - num2

def multiplication (num1, num2):
    return num1 * num2

def division (num1, num2):
    return num1 / num2

def main () :
    is_running = True

    print("-------Welcome To Calculater App-------")

    while is_running :
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")

        choice = int(input("Enter your choice : "))

        num1 = float(input("Enter number one : "))
        num2 = float(input("Enter number two : "))

        if choice == 1 :
            print("Addition result is :", addition(num1, num2))
        elif choice == 2:
            print("Subtraction result is : ", subtraction(num1, num2))
        elif choice == 3:
            print("Multiplication result is : ", multiplication(num1, num2))
        elif choice == 4:
            print(f"Division result is : {division(num1, num2)}" )
        else :
            print(f"{choice} is not valid!")
            print("Enter a correct option using above numbers(1/2/3/4).")
            choice = int(input("Enter your choice : "))

        last = input("Do you want to run again (y/n): ").lower()

        if last == 'y' :
            is_running = True
        elif last == 'n':
            is_running = False
        else :
            print("Enter a correct option")
            last = input("Do you want to run again (y/n): ").lower()
main()
# This function add numbers
def add(x,y):
    return x+y

# This function subtracts numbers
def subtract(x,y):
    return x-y

# This function multplies numbers
def multiply(x,y):
    return x*y

# This function divides numbers
def divide(x,y):
    return x/y

# This function exponentiate number
# def exponentiation(x,y):
#     return x^y


print("Select operation:")
print("1. Adding")
print("2. Subtracting")
print("3. Multiplying")
print("4. Dividing")
#print("5. Exponentiation")

while True:
    choice = input("Please insert number corresponding to action: ")
    if choice in ('1','2', '3', '4'):
        try:
            num1 = float(input("Insert first number: "))
            num2 = float(input("Insert second number: "))
        except:
            print("You inserted wrong number")

        if choice == '1':
            print(num1, " + ", num2 ," = ", add(num1, num2))

        elif choice == '2':
            print(num1, " - ", num2 ," = ", subtract(num1, num2))

        elif choice == '3':
            print(num1, " * ", num2 ," = ", multiply(num1, num2))

        elif choice == '4':
            print(num1, " / ", num2 ," = ", divide(num1, num2))

        # elif choice == '5':
        #     print(num1, " ^ ", num2 ," = ", exponentiation(num1, num2))

        next_calculation = input("Would you like to count once more? (yes/no)")
        if next_calculation == "no":
            break
    else:
        print("Wrong input")
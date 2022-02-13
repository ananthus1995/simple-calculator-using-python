def addition(x, y):
    return x+y
def mult(x, y):
    return x*y
def sub(x, y):
    return x-y
def division(x, y):
    return x/y

while True:

    print(f'{1} Addition')
    print(f'{2} Sub')
    print(f'{3} Multi')
    print(f'{4} Diviosn')

    option= int(input("please select option? "))
    if option in (1, 2, 3, 4):
        # count = int(input("continue? y/n"))
        if option==1:
                print("Addition")
                num1=float(input("enter first number"))
                num2=float(input("enter second number"))
                print(f'{num1}+{num2}=', addition(num1, num2))

        elif option==2:
                print("Substraction")
                num1 = float(input("enter first number"))
                num2 = float(input("enter second number"))
                print(f'{num1}-{num2}=', sub(num1, num2))
        elif option == 3:
                print("Multiplication")
                num1 = float(input("enter first number"))
                num2 = float(input("enter second number"))
                print(f'{num1}*{num2}=', mult(num1, num2))
        elif option == 4:
                print("Division")
                num1 = float(input("enter first number"))
                num2 = float(input("enter second number"))
                print(f'{num1}/{num2}=', division(num1, num2))
        count=input("continue y/n? ")
        if count=="n" or count=="N":
            break

    else:
        print("invalid option")




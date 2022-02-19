while(1):
    num1 = input("Enter the first number : ")
    num2 = input("Enter the second number : ")
    print("Choose any operator from the given : (+,-,/,*,%,//,**) and type (exit) to exit from the program")
    op = input("Enter the operator : ")

    if op=="+":
        sum=int(num1)+int(num2)
        print("Sum is "+ str(sum))
    elif op=="-":
        difference = int(num1)-int(num2)
        print("The difference is "+ str(difference))
    elif op=="*":
        product = int(num1)*int(num2)
        print("The product is "+ str(product))
    elif op=="//":
        quotient = int(num1)//int(num2)
        print("The quotient is "+ str(quotient))
    elif op=="**":
        power = int(num1)**int(num2)
        print("The difference is "+ str(power))
    elif op=="%":
        remainder = int(num1)%int(num2)
        print("The difference is "+ str(remainder))
    elif op=="exit":
        exit()
    else:
        print("Invalid operator")


a=int(input("Enter the first number: "))

b=int(input("Enter the second number: "))

choice=input("Enter the operator: ")

if choice=="+":
    print(f"sum of this {a+b}")

elif choice=="-":
    print(a-b)
    
elif choice=="*":
    print(a*b)
    
elif choice=="/":
    print(a/b)

elif choice=="%":
    print(a%b)
    
else:
    print("Invelid operator")
    




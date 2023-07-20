# Find the Largest Among Three Numbers.


num1 = int(input("Enter the number num1:"))
num2 = int(input("Enter the number num2:"))
num3 = int(input("Enter the number num3:"))
if(num1>num2) and (num1>num3):
    print(num1,"is Largest")
elif(num2>num1) and (num2>num3):
    print(num2,"is Largest")
elif(num3>num1) and (num3>num2):
    print(num3,"is Largest")
# program to revers a number

number = int(input("Enter thenumber: "))
revers_number = 0
while (number > 0):
    remainder = number % 10
    revers_number = (revers_number * 10) + remainder
    number = number // 10
print("The reverse number is : {}".format(revers_number))
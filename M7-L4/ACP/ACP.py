# Create a program to check if the user’s number given as an input is an Armstrong number.

num = int(input("Enter a number to check if it is an armstrong number: "))
temp = num
total = 0


while temp>0:
    floor = temp%10
    power = floor**3
    total = total + power
    temp = temp//10
    
if total == num:
    print(f"The {num} is an armstrong number")
else:
    print(f"The {num} is not armstrong number")


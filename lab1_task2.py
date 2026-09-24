number = int(input("enter the three-digit number:"))   
print("number is: ", number)
if 100 <= number <=999:
    units = number % 10
    tens = (number //10) % 10 
    print(f"Units digit: {units}, tens digit: {tens}")

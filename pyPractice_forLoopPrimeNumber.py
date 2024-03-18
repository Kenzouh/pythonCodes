
num = int(input("Input a number: "))

for i in range(2,num): #we start at 2 because no need to check for divisibility by 1. All even numbers are prime. So, the loop only needs to consider odd numbers.
    if num % i == 0:
        print(f"\n{num} is not a prime number; it's a composite number.")
        break
# this if statement will keep on running until it reaches the number before "num". If all possible numbers from 2~inputted number is done and the remainder is still not equal to "0", then. the else statement will run.
else:
    print(f"\n{num} is a prime number.")

num2 = num % i

print(f"\nModulus(remainder) of {num} is {num2}.")
# 🐍 Python Interview Questions

## Check whether a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")




## Find the largest of three numbers without max()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number:", largest)




## Factorial using a loop

num = int(input("Enter a number: "))
factorial = 1
# using for loop 
for i in range(1, num + 1):
    factorial = factorial * i
print("Factorial:", factorial)
# using while loop
while num>1:
    factorial = factorial*num
    num = num-1
print("Factorial:", factorial)



## Fibonacci series up to n terms
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    
    a, b = b, a + b




## Reverse a number
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)




## Check whether a number is palindrome
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")




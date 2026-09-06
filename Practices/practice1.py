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




## calculate number of vovels and consonant in a string

str = input('enter : ')

vowel=0
cons=0

for i in str.lower():

  if i.isalpha():
    if i in 'aeiou':
      vowel+=1
    else:
      cons+=1

print('vowels =',vowel,'\nConsonant =',cons)





## Reverse a string without slicing
str = input('enter : ')
rev = ''
for i in str.lower():
  rev = i+rev

print(rev)





## Frequency of each character in a string
str = input('enter : ')
freq = {}
for char in str.lower():
  if char in freq:
    freq[char] = freq[char]+1
  else:
    freq[char]=1
print(freq)
# 2nd/short technique
from collections import Counter
str = input('enter : ')
print(Counter(str))




## Remove duplicates from a list without set()
list = [1,2,2,3,4,5,5]

unique = []
for i in list:
  if i not in unique:
    unique.append(i)
print(unique)

# using set
list = [1,2,2,3,4,5,5]
set = set(list)
print(set)





## Find the second-largest number in a list
numbers = [10, 20, 5, 40, 30]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

unique.sort()

print("Second largest:", unique[-2])





## Find all even numbers using list comprehension
list = [1,2,3,4,6,8,7,9]
a = [x for x in list if x%2==0]
print(a)


































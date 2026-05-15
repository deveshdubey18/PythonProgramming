#concept of print function

# f-string  -> formated string
# name='chanmdan'
# age=22
# salary=50000
# print(f'hii my name is {name} age is {age} and salary is {salary}')

# # .format method 
# print('hii my name is {} age is {} salary is {}'.format(name,age,salary))

#concept of list : lst=[]
## list can cantain everything -> (int,float,string,boolean,list,tuple,set,dict,none)

# .append -> add values at last
# .insert -> add value at specific position

# lst=[]
# lst2=[1,2,3,4.5,'hii','world',True,[10,20,30],(1,2,3),{11,22,33},{'India':1000}]

### Control Flow :
# = -> assignment operator :assigning values
# == -> comparison operator : comparing

# name=input('Enter your name : ')

# if name=='devesh' :
#     print(f'Your name is {name}')

# coin_side=input("Enter coin side : ")
# if coin_side.lower()=='head':
#     print("You win the game.")  
# elif coin_side.lower()=='tail':
#     print('I won the game')
# else:
#     print('Enter valid coin side')

## concept of Indexing and Slicing
# str="Welcome to the world of Python programming"
# str1='Hello world'
# print(str1[::2])
# # slicing rule -> str[start:end:step]

''' 
write a program to print whether the value entered by user is palindrome or not
Logic :
1. ask user for input
2. reverse the string
3. compare both strings
4. if both are same then palindrome otherwise not palindrome
'''

string=input("Enter a string : ")
string1=string[::-1]

if string==string1:
    print(f"{string} is Palindrome")
else:
    print(f"{string} is not Palindrome")

# wap to ask useer to enter marks if marks > 90 then excellent ,marks>80 then good,marks>50 then pass else Fail. 
marks=int(input("Enter maeks"))
if marks>90:
    print("Excellent")
elif marks>80:
    print("good")
elif marks>50:
    print("pass")
else:
    print("Fail")




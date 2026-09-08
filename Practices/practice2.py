## Python DSA Methods

## Python List Methods
list = [10,20,40]
''' 
append() - Add element
extend() - Add multiple elements
insert() - Insert at position
remove() - Remove value
pop() - Remove by index
sort() - Sort list
reverse() - Reverse list
index() - Find index
count() - Count occurrences
'''

## String Methods
text = "Hello World"

'''
text.lower()
text.upper()
text.strip()
text.replace("Hello", "Hi")
text.split()
text.find("World")
text.count("l")
text.startswith("Hello")
text.endswith("World")
"is123".isalnum()
"123".isdigit()
"hello".isalpha()
'''


## Dictionary Methods
data = {
    "name": "Devesh",
    "age": 22
}

'''
data.keys()
data.values()
data.items()
data.get("name")
data.update({"age": 23})
data.pop("age")
'''

## Set Methods
a = {1, 2, 3}
b = {3, 4, 5}

'''
a.union(b)
a.intersection(b)
a.difference(b)

output- 
Union        → {1,2,3,4,5}
Intersection → {3}
Difference   → {1,2}
'''




## Linear Search
numbers = [10, 20, 30, 40, 50]

target = 30

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index:", i)
        break





## Binary Search
numbers = [10, 20, 30, 40, 50]

target = 40

low = 0
high = len(numbers) - 1

while low <= high:

    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Found at index:", mid)
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1






##























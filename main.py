print("hello world!")  # our first program to print output in terminal

# addition of two integers
a = 4
b = 5
c = a + b
print(c)

d = "shiva"
print(d[0])
print(type(d))

print("shivanand mishra\n")
print(bool(a + b))

# multiple assignment
e, f, g = "3", "4", "5"
print(e)

# tuple assignment
h = "4", "5", "6"
print(h)

i = j = k = "apple"

# list assignment
l = ["v", "z", "t"]
i = j = k = l
print(type(i))
print(i)

i, m, m = i
print(m)

n = [1, 4, 5, 6, 6, 77]
print(type(n))

# FUNCTION
def sum(o, p):
    global q
    return o + p


r = sum(1, 2)
print(r)

s = [2, 4, 6, 6, 4, 4, 9]
print(s[2:6])

# greeting function
def greet(name):
    print("good morning sir!", name)


greet("shiva")

t = 10
print("The number is : ", t)

# another function example
def love(name):
    global u
    print(f"I love {name}\n")


love("sham")

v = set()

w = ["a", 6, 7.8, True]
print(w[0:3])

# CONDITIONS
if w[3] == True:
    print("True")
else:
    print("false")

x = ["shiva", "mishra", "verma", "sourav", "hahaha"]
print(x[2:5])
print(x[-5:-2])
print(x[-4:0])

# LIST OPERATIONS
my_list = ["shiva", "mishra", "sahaj", "verma"]
my_list[1] = "sham"
print(my_list)

print("hello world!\n")

my_list[2:5] = "hey"

my_list.append("hey")
print(my_list)

my_list.insert(3, "hello")
print(my_list)

my_list.pop(3)
print(my_list)

my_list.remove("shiva")
print(my_list)

list_x = [2, 5, 6, 6, 6, 66]
my_list.extend(list_x)
print(my_list)

myList = [1, 1, 2, 3, 4, 5, 6]
lisForExtend = [2, 5, 6, 6]
print(f"{myList}\n{lisForExtend}\n")

myList.append("apple")
print(myList)

myList.insert(2, "banana")
print(myList)

myList.pop(2)
print(myList)

myList.remove("apple")
print(myList)

print("here is the final list", myList)

myList.clear()
print(myList)

myList.extend(lisForExtend)
print(myList)
print(myList)

print(myList.count(1))

for i in myList:
    print(i)

myList1 = [3, 5, 32, 5, 3]
myList1.sort()
print(myList1)

myList1.sort(reverse=True)
print(myList1)

text = "shiva"
print(text)
print(text.replace("v", "h"))

text1 = "hello"
print(text1.replace("hello", "world"))

y = "shiva"
age1 = 6

print("my name is {0} and my age is {1}".format(x, age1))
print(f"My name is {x}, and my age is {age1}")

z = 10
print(z)

z -= 2
print(z)

z += 2
print(z)

z *= 2
print(z)

# comparison operators
ab = 1
bc = 3

print(ab == bc)
print(ab != bc)
print(ab > bc)
print(ab < bc)
print(ab >= bc)
print(ab <= bc)

# identity operators
cd = [1, 2, 3]
de = cd
ef = [1, 2, 3]

print(cd is de)
print(cd is ef)

# SET
gh = {"hey", "hello", "hru", "hemlo"}
print(gh)

gh.add("hola")
print(gh)

gh.remove("hola")
print(gh)

for i in gh:
    print(i)

# DICTIONARY
student = {"name": "shiva", "age": 17, "grade": "A"}
print(student)
print(student["name"])
print(student.get("age"))

student["age"] = 21
student["city"] = "Delhi"
print(student)

student.pop("grade")
print(student)

del student["city"]
print(student)

for key, value in student.items():
    print(key, ":", value)

for i, x in student.items():
    print(i, ":", x)

# if-elif-else
age = 18
if age > 18:
    print("You are adult!")
elif age == 18:
    print("You are teen!")
elif age == 17:
    print("you are 17!")
else:
    print("you are not adult!")

# nested if-else
ij = 15
if ij > 10:
    print("x is greater than 10!")
    if ij > 20:
        print("x is also greater than 20!")
    else:
        print("x is not greater than 20!")

# even or odd
jk = int(input("Enter the number : "))
if jk % 2 == 0:
    print("even")
else:
    print("odd")

# driving eligibility
age2 = int(input("Enter the age : "))
if age2 > 18:
    print("You are eligible for driving!")
else:
    print("You are not eligible for driving!")

# largest among three numbers
largest = 0
lm = 2
mn = 1
no = 5

if lm > mn and lm > no:
    largest += lm
elif mn > lm and mn > no:
    largest += lm
else:
    largest += no

print(f"the largest number is {largest}")

# FOR LOOP
for i in range(0, 10):
    print("saitm\n")

for i in range(1, 10, 2):
    print(i)

# nested for loop
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i = {i}, j = {j}\n")

# break statement
for i in range(6):
    if i == 4:
        break
    print(i)

# continue statement
for i in range(6):
    if i == 3:
        continue
    print(i)

for i in range(1, 21):
    print(i)

for i in range(2, 31, 2):
    print(i)

# iterating through a list
colours = ["black", "blue", "white"]
for i in colours:
    print(i)

# continue and break example
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

# Loop with break statement
for i in range(0, 10):
    if i == 7:
        break
    print(i)

# Nested loops demonstration
for i in range(1, 4):
    for j in range(1):
        for k in range(1):
            print(f"i = {i}, j = {j}, k = {k}")

# FUNCTIONS
def greet(name):
    print(f"good morning! {name}")

greet("shiva")

def sum(a, b):
    return a + b

print(sum(2, 4))

def greet(name="shiva", age=17):
    print(f"name = {name}, age = {age}\n")

greet(name="shiva", age=17)

def mul(a, b):
    return a * b

print(mul(3, 4))

def sub(a, b):
    return a - b

print(sub(5, 2))

def div(a, b):
    return a / b

print(div(8, 2))

# Demonstrating global variable
def var():
    op = 3
    global qr
    qr = 4

# print(qr)

# CLASS
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.color} {self.brand} is driving!")

car1 = Car("BMW", "White")
car1.drive()

# ARRAY MODULE
import array
numbers = array.array('i', [1, 3, 2, 4, 5])
print(numbers[1])

# NUMPY DEMONSTRATION
import os
os.system("pip install numpy")

from numpy import random

otp = random.randint(1000, 9999)
print(otp)

ran = random.rand()
print(ran)
print(type(ran))

# Random number list
rs = []
for i in range(1, 9):
    tu = random.randint(0, 10)
    rs.append(tu)

rs.sort()
print(rs)

# Random arrays of different dimensions
uv = random.randint(100, size=(5))
print(uv)

vw = random.randint(100, size=(3, 5))
print(vw)

wx = random.randint(100, size=(2, 3, 5))

# Correct array creation
numbers = array.array('i', [1, 2, 3, 4, 5])
print(numbers)

# Random numbers using numpy
xy = random.randint(100)
print(xy)

yz = random.rand()
print(yz)

abc = random.randint(100, size=(5))
print(abc)

efg = random.randint(100, size=(3, 5))
print(efg)

ghi = random.randint(100, size=(2, 2, 3, 5))
print(ghi)

ijk = random.choice([3, 5, 7, 9], size=(2, 3, 5))
print(ijk)

# PANDAS DEMONSTRATION
import pandas as pd

data = [10, 20, 30, 40]
klm = pd.Series(data)
print(klm)

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "City": ["Delhi", "Mumbai", "Chennai", "Kolkata"]
}

mno = pd.DataFrame(data)
print(mno)

# Reading a CSV file
opq = pd.read_csv('crocks.csv')
print(opq.head())
print(opq.tail())
# 1. Data Types
# 1. Find the data type of every value in a mixed list.
my_list = [10, 20.5, "Python", True, [1, 2], (3, 4)]

for value in my_list:
    print(value, ":",type(value))

# 2. Convert a nested list into a tuple of tuples.
my_list = [[1, 2], [3, 4], [5, 6]]
result = tuple(tuple(i) for i in my_list)
print(result)  

# 3.Remove duplicate values while preserving original order.
my_list=[10,20,10,"python",30,"python",20]
new_list=[]
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print("List Without duplicates value:",new_list)

# 2. Operators
# 4. Check whether a number is a power of 2.

n=int(input("Enter the number:"))

if n > 0 and (n&(n-1))==0:
    print("Power of 2")
else:
    print("Not power of 2 ")

# 5. Swap two numbers using bitwise XOR.
a=10
b=20

a=a^b
b=a^b
a=a^b

print("After swaping")
print("a=",a)
print("b=",b)

# 6. Check whether a number is divisible by both 4 and 6.
n=int(input("Enter the number:"))

if n%4==0 and n%6==0:
    print("divisible by 4 and 6")
else:
    print("not divisible by 4 and 6 ")


# 7. Calculate electricity bill using different unit rates.
units=int (input("Enter the number of units consumened:"))

if units<=100:
    bill=units*3
elif units<=200:
    bill=(units*3)+(units-100)
else:
    bill=(units*3)+(units*5)+(units-200)*7
print("Total electrical Bill:",bill,"Rs")


# 3. Conditional Statements
# 8. Check whether three sides can form a triangle.
a=int(input("Enter the first side of triangle:"))
b=int(input("Enter the second side of triangle:"))
c=int(input("Enter the third side of triangle:"))

if a+b>c and a+c>b and b+c>a:
    print("Triangle valid")
else:
    print("Not valid Triangle")

# 9. Determine the type of triangle.
a=int(input("Enter the first side of triangle:"))
b=int(input("Enter the second side of triangle:"))
c=int(input("Enter the third side of triangle:"))

if a <= 0 or b<= 0 or c <= 0:
    print("Invalid Triangle")
elif a+b<=c and a+c<=b and b+c<=a:
    print("Invalid triangle")
elif a == b == c:
 print("Euilateral trangle")
elif a==b and b==c and a==c:
 print("Issoscales triangle")
else:
 print("Scalene Triangle")

# 10. Create a simple ATM menu.
balance = 5000

while True:
    print("\n1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter amount: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdraw successful")
        else:
            print("Invalid amount or insufficient balance")

    elif choice == 2:
        amount = int(input("Enter amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

            

    elif choice == 3:
        print("Current balance:", balance)

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Invalid choice")

# 11. Calculate income tax based on different tax slabs.
income = float(input("Enter annual income: "))

if income <= 300000:
    tax = 0

elif income <= 600000:
    tax = (income - 300000) * 0.05

elif income <= 900000:
    tax = 15000 + (income - 600000) * 0.10

else:
    tax = 45000 + (income - 900000) * 0.15

print("Income tax:", tax)

#12. Menu-driven calculator using if-elif.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Addition:", a + b)

elif choice == 2:
    print("Subtraction:", a - b)

elif choice == 3:
    print("Multiplication:", a * b)

elif choice == 4:
    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")

# 4. Loops
# 13. Print all prime numbers between 1 and n.
n = int(input("Enter n: "))

for num in range(2, n + 1):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, end=" ")

# 14. Find factorial using a loop.
n = int(input("Enter a number: "))

fact = 1

if n < 0:
    print("Factorial not possible")

else:
    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial:", fact)

# 15. Print Fibonacci series up to n terms.
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

#16. Check whether a number is an Armstrong number.
n = int(input("Enter a number: "))

temp = n
power = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** power
    temp = temp // 10

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

#17. Reverse a number and check palindrome.
n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse:", reverse)

if original == reverse:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")

# 18. Find GCD of two numbers.
from sympy import Function


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = abs(a)
b = abs(b)

while b != 0:
    a, b = b, a % b

print("GCD:", a)

#5. Functions
#19. Function to check whether a string is palindrome.
def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


text = input("Enter a string: ")

palindrome(text)

#20. Function to count vowels and consonants.
def count_letters(s):
    vowels = 0
    consonants = 0

    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)


text = input("Enter a string: ")

count_letters(text)

#21. Function to calculate simple and compound interest.
def interest(p, r, t):
    si = (p * r * t) / 100

    amount = p * (1 + r / 100) ** t
    ci = amount - p

    print("Simple Interest:", si)
    print("Compound Interest:", ci)


p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

interest(p, r, t)

# 22. Function to return all factors of a number.
def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")


n = int(input("Enter a number: "))

factors(n)

#23. Function to find the second-largest number in a list.
def second_largest(numbers):
    numbers = sorted(set(numbers), reverse=True)

    if len(numbers) >= 2:
        return numbers[1]
    else:
        return "Second largest does not exist"


my_list = [10, 20, 40, 30, 40]

print("Second largest:", second_largest(my_list))

# 6. Lists
# 24. Merge two lists without duplicates.
list1 = [10, 20, 30]
list2 = [20, 40, 50]

result = []

for i in list1 + list2:
    if i not in result:
        result.append(i)

print("Merged list:", result)

#25. Find second-largest and second-smallest elements.
numbers = [10, 20, 30, 40, 50]

numbers = sorted(set(numbers))

if len(numbers) >= 2:
    print("Second smallest:", numbers[1])
    print("Second largest:", numbers[-2])
else:
    print("Not enough distinct elements")


# 26. Rotate a list to the left by k positions.
my_list = [1, 2, 3, 4, 5]

k = int(input("Enter rotation value: "))

k = k % len(my_list)

result = my_list[k:] + my_list[:k]

print("Rotated list:", result)

# 27. Separate even and odd numbers into two lists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)

#28. Find common elements between two lists.
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

common = []

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print("Common elements:", common)

# 7. Tuples & Sets
# 29. Count frequency of each element in a tuple.
my_tuple = (10, 20, 10, 30, 20, 10)

for i in set(my_tuple):
    print(i, ":", my_tuple.count(i))

# 30. Find union, intersection and difference of two sets.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Union:", set1 | set2)

print("Intersection:", set1 & set2)

print("Difference:", set1 - set2)

# 31. Check whether one set is a subset of another.
set1 = {10, 20}
set2 = {10, 20, 30, 40}

if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")

# 8. Dictionaries
# 32. Count frequency of words in a sentence.
sentence = input("Enter a sentence: ")

words = sentence.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)

# 33. Create a dictionary from two lists.
keys = ["name", "age", "city"]
values = ["Rutik", 21, "Nashik"]

my_dict = dict(zip(keys, values))

print(my_dict)

#34. Sort a dictionary by its values.
my_dict = {
    "Apple": 50,
    "Banana": 20,
    "Mango": 40,
    "Orange": 30
}

result = dict(sorted(my_dict.items(), key=lambda x: x[1]))

print("Sorted dictionary:", result)

# 9. File Handling
# 35. Count lines, words and characters in a text file.
file = open("sample.txt", "r")

content = file.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", characters)

file.close()

#36. Copy only even-numbered lines from one file to another.
source = open("input.txt", "r")
destination = open("output.txt", "w")

for line_number, line in enumerate(source, start=1):
    if line_number % 2 == 0:
        destination.write(line)

source.close()
destination.close()

print("Even-numbered lines copied successfully")


# 10. Exception Handling
# 37. Handle invalid integer input using try-except.
try:
    n = int(input("Enter an integer: "))
    print("Number:", n)

except ValueError:
    print("Invalid input! Please enter an integer.")

# 38. Handle file-not-found errors.
try:
    file = open("sample.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:
    print("Error: File not found")

# 11. Modules
# 39. Create a random password generator.
import random
import string

length = int(input("Enter password length: "))

if length < 4:
    print("Password length must be at least 4")

else:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated password:", password)

# 40. Calculate number of days between two dates using datetime.
from datetime import datetime

date1 = input("Enter first date (YYYY-MM-DD): ")
date2 = input("Enter second date (YYYY-MM-DD): ")

d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")

difference = abs((d2 - d1).days)

print("Number of days:", difference)





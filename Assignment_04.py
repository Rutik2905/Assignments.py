
# 1. Check whether a number is Even or Odd
num = int(input("Enter the number:"))
if num % 2 == 0:
    print(f"{num} is Even number")
else:
    print(f"{num} is Odd number")


# 2. Find the Largest of Three Numbers
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
c = int(input("Enter the number:"))

if a >= b and a >= c:
    print(f"{a} is Greater")
elif b >= c and b >= a:
    print(f"{b} is Greater")
else:
    print(f"{c} is Greater")


# 3. Check Whether a Given Number is Prime
num = int(input("Enter the number:"))
if num <= 1:
    print(f"{num} is not a prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


# 4. Print the Fibonacci Series up to n Terms
n = int(input("Enter the number:"))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


# 5. Find the Factorial of a Number Using a Loop
n = int(input("Enter the number:"))
fact = 1

if n < 0:
    print("Not factorial")
else:
    for i in range(1, n + 1):
        fact = fact * i

    print(f"Factorial = {fact}")


# 6. Reverse a String Without Using [::-1]
text = input("Enter a string:")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(f"Reversed string: {reversed_text}")


# 7. Check Whether a String is a Palindrome
text = input("Enter the string:")
cleaned = text.lower().replace(" ", "")

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not palindrome.")


# 8. Count the Number of Vowels and Consonants in a String
text = input("Enter the string:").lower()
vowels = "aeiou"
v_count = 0
c_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print(f"Vowels = {v_count}, Consonants = {c_count}")


# 10. Find Largest and Smallest Element Without max() or min()
numbers = []
n = int(input("Range of the list:"))

for i in range(n):
    value = int(input("Enter the value:"))
    numbers.append(value)

larg = numbers[0]
small = numbers[0]

print("Numbers =", numbers)

for num in numbers:
    if num > larg:
        larg = num
    if num < small:
        small = num

print(f"Largest = {larg}, Smallest = {small}")


# 11. Remove Duplicates from a List
lists = [1, 2, 2, 1, 3, 4, 5, 4, 5, 6, 6]
uniq_list = []

for list in lists:
    if list not in uniq_list:
        uniq_list.append(list)

print(f"Unique_list = {uniq_list}")


# 12. Count Element Occurrence in a List Using a Dictionary
items = ["apple", "banana", "apple", "orange", "Bnanana", "apple"]
counts = {}

for item in items:
    counts[item] = counts.get(item, 0) + 1

print("Element counts:", counts)


# 13. Find the Second-Largest Number in a List
numbers = [12, 45, 1, 89, 89, 34, 67]
unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("No second-largest number exists.")
else:
    unique_numbers.sort()
    print(f"Second-largest number: {unique_numbers[-2]}")


# 14. Sort a List Without Using sort() or sorted()
numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(f"Sorted list: {numbers}")


# 15. Function Returning Only Even Numbers from a List
def get_even_numbers(num_list):
    return [num for num in num_list if num % 2 == 0]


sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:", get_even_numbers(sample))


# 16. Find the Frequency of Each Character in a String
text = input("Enter a string: ")
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print("Character frequencies:", freq)


# 17. Check Whether Two Strings are Anagrams
str1 = input("Enter first string: ").lower().replace(" ", "")
str2 = input("Enter second string: ").lower().replace(" ", "")

if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


# 18. Find All Duplicate Values in a List
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]
seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicate values:", list(duplicates))


# 19. Find the Longest Word in a Sentence
sentence = input("Enter a sentence: ")
words = sentence.split()

if words:
    longest_word = max(words, key=len)
    print(f"Longest word: '{longest_word}' (Length: {len(longest_word)})")
else:
    print("No words entered.")


# 20. Student Marks, Percentage, Grade & Pass/Fail Program
marks = []
subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]

for subject in subjects:
    score = float(input(f"Enter marks for {subject} (out of 100): "))
    marks.append(score)

total = sum(marks)
percentage = (total / 500) * 100

# Determine Pass/Fail (minimum 35 marks required per subject)
passed = all(m >= 35 for m in marks)

# Assign Grade
if not passed:
    grade = "F"
elif percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "E"

print("\n--- Student Result ---")
print(f"Total Marks : {total} / 500")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade : {grade}")
print(f"Status : {'PASS' if passed else 'FAIL'}")

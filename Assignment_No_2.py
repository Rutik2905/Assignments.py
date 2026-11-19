# #odd Even
def is_even(n):
  if n%2==0:
    return "even"
  else:
    return "odd"
n=int(input("Enter the Number:"))
print(is_even(n))

# #Largest of two numbers
def largest(a,b):
  if a>b:
    return a
  else:
    return b
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("print largest number:",largest(a,b))

#print numbers from 1 to n 
def print_numbers(n):
   for i in range(1,n+1):
        print(i)
n=int(input("Enter the number:"))
print_numbers(n)

# #sum of numbers
def total_sum(n):
   total = 0
   for i in range(1,n+1):
      total = total+i
   return total

n=int(input("Enter the number:"))
print("count", total_sum(n))

# multiplication table
def multi_table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
n=int(input("Enter the number:"))
multi_table(n)

# #count even numbers
def count_even(n):
    count=0
    for i in n:
        if i % 2==0:
            count +=1
    return count
n=[1,2,3,4,5,6,7,8,9]
print(count_even(n))

# # maximum number in a list
def max_number(numbers):
    largest=numbers[0]
    for i in numbers:
        if i>largest:
            largest=i
    return largest
print("Largest:", max_number([1,2,8,3,4,5,6]))

#FizzBuzz
def fizzbuzz():
   for i in range(1,101):
      if i%3==0 and i%5==0:
         print( "FizzBuzz")
      elif i%3==0:
         print( "Fizz")
      elif i%5==0:
         print( "Buzz")
      else:
         print(i)
fizzbuzz()


# #pallindrom
def palindrom(s):
    if s==s[::-1]:
        return True
    else:
        return False
s=input("Enter the String:")
print(palindrom(s))

# #count Vovels
def count_vovels(s):
    count=0
    for i in s:
      if i.lower() in "aeoui":
         count=count+1
    return count
s=input("Enter a string:")
print("Total vowels:",count_vovels(s))

# #Second largest Number
def second_largest(numbers):
    largest=float('-inf')
    second =float('-inf')
    for i in numbers:
      if i > largest:
          second=largest
          largest=i
      elif i>second and i !=largest:
          second=i
    return second

print(second_largest([10,20,30,40,45,50]))

#Guessing Game
import random
def gussing_game():
    number = random.randint(1, 10)

    while True:
        guess=int(input("Guess number between 1 and 10:"))
        if guess==number:
          print("Correct Guess!")
          break
        elif guess < number:
          print("Too Low ! Try Again.")
        else :
          print("Too High! Try Again.")
gussing_game()

# grade marks
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

marks = int(input("Enter your marks: "))
print("Your Grade:", grade(marks))


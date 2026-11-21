# Python Assignment: 30 If-Else Programs
# Run this file and enter the exercise number (1-30) to execute that program.

def program1():
    n = int(input("Enter a number: "))
    if n > 0:
        print("Positive number")
    elif n < 0:
        print("Negative number")
    else:
        print("Zero")


def program2():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def program3():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if a > b:
        print("Greater:", a)
    elif b > a:
        print("Greater:", b)
    else:
        print("Both are equal")


def program4():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if a >= b and a >= c:
        print("Greatest:", a)
    elif b >= a and b >= c:
        print("Greatest:", b)
    else:
        print("Greatest:", c)


def program5():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Eligible for voting")
    else:
        print("Not eligible for voting")


def program6():
    year = int(input("Enter year: "))
    if year % 400 == 0:
        print("Leap year")
    elif year % 100 == 0:
        print("Not a leap year")
    elif year % 4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")


def program7():
    ch = input("Enter a character: ")
    if len(ch) == 1 and ch.isalpha():
        if ch.lower() in "aeiou":
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("Invalid character")


def program8():
    n = int(input("Enter a number: "))
    if n % 5 == 0 and n % 11 == 0:
        print("Divisible by 5 and 11")
    else:
        print("Not divisible by 5 and 11")


def program9():
    n = int(input("Enter a number: "))
    if n % 3 == 0 and n % 7 == 0:
        print("Multiple of 3 and 7")
    else:
        print("Not a multiple of both 3 and 7")


def program10():
    marks = int(input("Enter your marks: "))
    if marks < 0 or marks > 100:
        print("Invalid marks")
    elif marks >= 90:
        print("Grade A")
    elif marks >= 80:
        print("Grade B")
    elif marks >= 70:
        print("Grade C")
    elif marks >= 60:
        print("Grade D")
    else:
        print("Grade F")


def program11():
    ch = input("Enter a character: ")
    if len(ch) == 1 and ch.isupper():
        print("Uppercase")
    elif len(ch) == 1 and ch.islower():
        print("Lowercase")
    else:
        print("Not an alphabet")


def program12():
    ch = input("Enter an alphabet: ").lower()
    if len(ch) != 1 or not ch.isalpha():
        print("Invalid input")
    elif ch == 'a':
        print("Vowel")
    elif ch == 'e':
        print("Vowel")
    elif ch == 'i':
        print("Vowel")
    elif ch == 'o':
        print("Vowel")
    elif ch == 'u':
        print("Vowel")
    else:
        print("Consonant")


def program13():
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        print("Valid triangle")
    else:
        print("Invalid triangle")


def program14():
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle")
    elif a == b and b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")


def program15():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    d = int(input("Enter fourth number: "))
    if a >= b and a >= c and a >= d:
        print("Largest:", a)
    elif b >= a and b >= c and b >= d:
        print("Largest:", b)
    elif c >= a and c >= b and c >= d:
        print("Largest:", c)
    else:
        print("Largest:", d)


def program16():
    n = int(input("Enter a number: "))
    if 100 <= abs(n) <= 999:
        print("Three-digit number")
    else:
        print("Not a three-digit number")


def program17():
    # Assumed practice rates: first 100 units Rs. 5/unit,
    # next 100 units Rs. 7/unit, above 200 units Rs. 10/unit.
    units = int(input("Enter electricity units: "))
    if units < 0:
        print("Invalid units")
    elif units <= 100:
        bill = units * 5
        print("Electricity bill:", bill)
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
        print("Electricity bill:", bill)
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
        print("Electricity bill:", bill)


def program18():
    # Simplified practice slabs only; not official tax advice.
    income = float(input("Enter your income: "))
    if income < 0:
        print("Invalid income")
    elif income <= 250000:
        tax = 0
        print("Practice tax amount:", tax)
    elif income <= 500000:
        tax = income * 0.05
        print("Practice tax amount:", tax)
    elif income <= 1000000:
        tax = income * 0.20
        print("Practice tax amount:", tax)
    else:
        tax = income * 0.30
        print("Practice tax amount:", tax)


def program19():
    m1 = int(input("Enter subject 1 marks: "))
    m2 = int(input("Enter subject 2 marks: "))
    m3 = int(input("Enter subject 3 marks: "))
    if 0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100:
        if m1 >= 35 and m2 >= 35 and m3 >= 35:
            print("Student passed")
        else:
            print("Student failed")
    else:
        print("Invalid marks")


def program20():
    n = int(input("Enter a number: "))
    start = int(input("Enter starting range: "))
    end = int(input("Enter ending range: "))
    if start <= end and start <= n <= end:
        print("Number is within range")
    else:
        print("Number is outside range or range is invalid")


def program21():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    if op == '+':
        print("Addition:", a + b)
    elif op == '-':
        print("Subtraction:", a - b)
    elif op == '*':
        print("Multiplication:", a * b)
    elif op == '/':
        if b != 0:
            print("Division:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operator")


def program22():
    year = int(input("Enter year: "))
    if year % 100 == 0 and year % 400 == 0:
        print("Century leap year")
    elif year % 100 == 0:
        print("Century year, but not a leap year")
    else:
        print("Not a century year")


def program23():
    month = int(input("Enter month number (1-12): "))
    if month in [3, 4, 5]:
        print("Summer season")
    elif month in [6, 7, 8, 9]:
        print("Rainy season")
    elif month in [10, 11]:
        print("Autumn season")
    elif month in [12, 1, 2]:
        print("Winter season")
    else:
        print("Invalid month")


def program24():
    month = int(input("Enter month number: "))
    year = int(input("Enter year: "))
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print("29 days")
        else:
            print("28 days")
    elif month in [4, 6, 9, 11]:
        print("30 days")
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        print("31 days")
    else:
        print("Invalid month")


def program25():
    password = input("Enter password: ")
    has_digit = any(ch.isdigit() for ch in password)
    if len(password) >= 8 and has_digit:
        print("Valid password")
    else:
        print("Invalid password")
        print("Use at least 8 characters and one digit.")


def program26():
    age = int(input("Enter your age: "))
    if age < 0:
        print("Invalid age")
    elif age < 5:
        print("Free ticket")
    elif age <= 17:
        print("Ticket price: Rs. 50")
    elif age < 60:
        print("Ticket price: Rs. 100")
    else:
        print("Ticket price: Rs. 70")


def program27():
    amount = float(input("Enter purchase amount: "))
    if amount < 0:
        print("Invalid amount")
    elif amount > 5000:
        discount = amount * 0.20
        print("Discount:", discount)
        print("Final amount:", amount - discount)
    elif amount > 3000:
        discount = amount * 0.10
        print("Discount:", discount)
        print("Final amount:", amount - discount)
    elif amount > 1000:
        discount = amount * 0.05
        print("Discount:", discount)
        print("Final amount:", amount - discount)
    else:
        print("No discount")
        print("Final amount:", amount)


def program28():
    age = int(input("Enter your age: "))
    eyesight = input("Is your eyesight good? (yes/no): ").lower()
    if age >= 18 and eyesight == "yes":
        print("Eligible for driving license")
    else:
        print("Not eligible for driving license")


def program29():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "12345":
        print("Login successful")
    else:
        print("Invalid username or password")


def program30():
    while True:
        print("\\n----- MENU -----")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Thank you!")
            break
        elif choice in [1, 2, 3, 4]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
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


programs = {
    1: program1, 2: program2, 3: program3, 4: program4, 5: program5,
    6: program6, 7: program7, 8: program8, 9: program9, 10: program10,
    11: program11, 12: program12, 13: program13, 14: program14,
    15: program15, 16: program16, 17: program17, 18: program18,
    19: program19, 20: program20, 21: program21, 22: program22,
    23: program23, 24: program24, 25: program25, 26: program26,
    27: program27, 28: program28, 29: program29, 30: program30
}

if __name__ == "__main__":
    print("PYTHON IF-ELSE ASSIGNMENT")
    print("Choose a program number from 1 to 30.")
    print("Enter 0 to exit.")

    while True:
        choice = int(input("\\nEnter program number (1-30, 0 to exit): "))

        if choice == 0:
            print("Goodbye!")
            break
        elif choice in programs:
            print("\\n--- Program", choice, "---")
            programs[choice]()
        else:
            print("Invalid choice. Please enter a number from 1 to 30.")

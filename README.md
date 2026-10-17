# 🐍 Python OOP Practicals

This repository contains all **15 practicals** from the *Object Oriented Programming using Python* syllabus, along with one extra practical: **Simple Calculator**.

Each practical includes its aim, Python source code, sample input/output, and a placeholder for the output screenshot.

## 📚 Practicals List

| No. | Practical Name | Description |
|---:|---|---|
| 1 | Quadratic Equation | Find the roots of a quadratic equation. |
| 2 | Prime Numbers | Check prime numbers, generate primes up to `n`, and print the first `n` primes. |
| 3 | Star Pyramid | Print a star pyramid and a reverse pyramid. |
| 4 | Character Checking | Identify letters, digits, special characters, letter case, and digit names. |
| 5 | String Operations | Count, replace, and remove character occurrences. |
| 6 | Swap String Characters | Swap the first `n` characters of two strings. |
| 7 | Substring Indices | Find all occurrences of a substring and return their indices. |
| 8 | Even Number Cubes | Calculate cubes of even integers using loops and list comprehension. |
| 9 | File Handling | Count characters, words, and lines; calculate character frequency; reverse words; split lines into files. |
| 10 | Dictionary of Cubes | Create a dictionary containing numbers as keys and their cubes as values. |
| 11 | Tuple Operations | Split tuples, select even values, concatenate tuples, and find maximum and minimum values. |
| 12 | Employee Class | Create an Employee class with employee details and salary calculation. |
| 13 | 2D Point Class | Calculate the distance between two 2D points. |
| 14 | 3D Point Inheritance | Inherit the 2D point class and calculate 3D distance. |
| 15 | Name Validation | Raise and handle exceptions for invalid names. |
| 16 | Simple Calculator (Extra) | Perform addition, subtraction, multiplication, and division. |

## 🛠️ Requirements

- Python 3.x
- VS Code, IDLE, PyCharm, or another Python editor

## ▶️ How to Run

Save each program in a `.py` file and execute it using:

```bash
python filename.py
```

---

## Practical 1: Quadratic Equation

**Aim:** Find the roots of a quadratic equation.

### Source Code

```python
import math 

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

d = b**2 - 4*a*c

if a == 0:
    print("Not a quadratic equation")
elif d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are real and different")
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif d == 0:
    root = -b / (2 * a)
    print("Roots are real and equal")
    print("Root =", root)
else:
    real = -b / (2 * a)
    imag = math.sqrt(-d) / abs(2 * a)
    print("Roots are complex")
    print("Root 1 =", complex(real, imag))
    print("Root 2 =", complex(real, -imag))
```

### Sample Test

```text
Enter the coefficient a: 12
Enter the coefficient b: 24
Enter the coefficient c: 48
Roots are complex
Root 1 = (-1+1.7320508075688774j)
Root 2 = (-1-1.7320508075688774j)
```

### Output Screenshot

<img width="367" height="132" alt="image" src="https://github.com/user-attachments/assets/e9432d43-5051-4886-b6e9-b9a3de57a9ff" />


---

## Practical 2: Prime Numbers

**Aim:** Check whether a number is prime, generate primes up to `n`, and print the first `n` primes.

### Source Code

```python

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def primes_till_n(n):
    print("Prime numbers till", n, "are:")
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=" ")
    print()


def first_n_primes(n):
    print("First", n, "prime numbers are:")
    count = 0
    num = 2

    while count < n:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1
    print()


# Main program
n = int(input("Enter a number: "))

# (a) Check if n is prime
if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")

# (b) Generate all prime numbers till n
primes_till_n(n)

# (c) Generate first n prime numbers
if n > 0:
    first_n_primes(n)
else:
    print("Enter a positive number for the first n primes.")

```

### Sample Test

```text
Enter a number: 12
12 is not a prime number
Prime numbers till 12 are:
2 3 5 7 11 
First 12 prime numbers are:
2 3 5 7 11 13 17 19 23 29 31 37 
```

### Output Screenshot
<img width="347" height="127" alt="image" src="https://github.com/user-attachments/assets/6d52240f-db92-4839-bc7d-5a274682a116" />




---
  
## Practical 3: Star Pyramid

**Aim:** Print a star pyramid and a reverse pyramid.

### Source Code

```python
n = int(input("Enter the number of rows: "))

# Pyramid
print("Pyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# Reverse Pyramid
print("Reverse Pyramid:")
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
```

### Sample Test

```text
Enter number of rows: 3
Pyramid:
  *
 * *
* * *
Reverse Pyramid:
* * *
 * *
  *
```

### Output Screenshot

<img width="407" height="187" alt="image" src="https://github.com/user-attachments/assets/c7b6179f-5b79-4162-b6c6-eddf224b7cf6" />


---

## Practical 4: Character Checking

**Aim:** Identify whether a character is a letter, digit, or special character. Display letter case or the digit name.

### Source Code

```python
ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only one character.")

elif ch.isalpha():
    print("The character is a letter.")

    if ch.isupper():
        print("It is an uppercase letter.")
    else:
        print("It is a lowercase letter.")

elif ch.isdigit():
    print("The character is a numeric digit.")

    digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
              "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

    print("Digit in words:", digits[int(ch)])

else:
    print("The character is a special character.")

```

### Sample Test

```text
Enter a character: 9 
The character is a numeric digit.
Digit in words: NINE
```

### Output Screenshot

<img width="370" height="61" alt="image" src="https://github.com/user-attachments/assets/78f041f9-a60c-4b64-8845-53d9d7cfef25" />


---

## Practical 5: String Operations

**Aim:** Find character frequency, replace a character, remove its first occurrence, and remove all occurrences.

### Source Code

```python
# Accept a string
s = input("Enter a string: ")

# (a) Find frequency of a character
ch = input("Enter character to find frequency: ")
print("Frequency =", s.count(ch))

# (b) Replace a character
old = input("Enter character to replace: ")
new = input("Enter new character: ")
print("After replacement:", s.replace(old, new))

# (c) Remove the first occurrence of a character
ch = input("Enter character to remove (first occurrence): ")
print("After removing first occurrence:", s.replace(ch, "", 1))

# (d) Remove all occurrences of a character
ch = input("Enter character to remove (all occurrences): ")
print("After removing all occurrences:", s.replace(ch, ""))
```

### Sample Test

```text
Enter a string: banana
Enter character to find frequency: a
Frequency = 3
Enter character to replace: 0
Enter new character: o
After replacement: banana
Enter character to remove (first occurrence): a
After removing first occurrence: bnana
Enter character to remove (all occurrences): a
After removing all occurrences: bnn
```

### Output Screenshot

<img width="516" height="212" alt="image" src="https://github.com/user-attachments/assets/15b53c59-447a-476f-824f-bbfb2fb265b1" />


---

## Practical 6: Swap First n Characters

**Aim:** Swap the first `n` characters of two strings.

### Source Code

```python
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter the value of n: "))

if 0 <= n <= len(s1) and n <= len(s2):
    a = s1[:n]
    b = s2[:n]

    s1 = b + s1[n:]
    s2 = a + s2[n:]

    print("First string after swapping:", s1)
    print("Second string after swapping:", s2)
else:
    print("Invalid value of n")
```

### Sample Test

```text
Enter first string: hello
Enter second string: world
Enter n: 2
First string: wollo
Second string: herld
```

### Output Screenshot

<img width="382" height="105" alt="image" src="https://github.com/user-attachments/assets/4582bb82-7905-4f2e-8744-fb1468484949" />


---

## Practical 7: Find Substring Indices

**Aim:** Return all indices where the second string occurs in the first string. Return `-1` if it is absent.

### Source Code

```python
def find_indices(text, sub):
    if sub == "":
        return list(range(len(text) + 1))

    indices = []
    start = 0

    while True:
        index = text.find(sub, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1

    return indices if indices else -1

text = input("Enter main string: ")
sub = input("Enter substring: ")

print("Indices:", find_indices(text, sub))
```

### Sample Test

```text
Enter main string: banana
Enter substring: ana
Indices: [1, 3]
```

### Output Screenshot

<img width="367" height="65" alt="image" src="https://github.com/user-attachments/assets/b8078c63-4ca4-47f8-861b-937e1fb06ce4" />


---

## Practical 8: Cubes of Even Integers

**Aim:** Create a list of cubes of even integers using a loop and list comprehension.

### Source Code

```python
items = input("Enter numbers separated by spaces: ").split()
numbers = []

for item in items:
    try:
        numbers.append(int(item))
    except ValueError:
        pass

cubes_loop = []
for n in numbers:
    if n % 2 == 0:
        cubes_loop.append(n**3)

cubes_comprehension = [
    n**3 for n in numbers if n % 2 == 0
]

print("Using loop:", cubes_loop)
print("Using list comprehension:", cubes_comprehension)
```

### Sample Test

```text
Enter numbers separated by spaces: 1 2 3 4 5 6 7 
Using loop: [8, 64, 216]
Using list comprehension: [8, 64, 216]
```

### Output Screenshot

<img width="497" height="62" alt="image" src="https://github.com/user-attachments/assets/4be03f4c-b53a-491f-a83c-623c5070721f" />


---

## Practical 9: File Handling

**Aim:** Count characters, words, and lines; calculate character frequency; reverse word order; and separate even and odd lines into files.

Create a text file named `input.txt` in the same directory before running the program.

### Source Code

```python
# Read the file
f = open("data.txt", "r")
text = f.read()
f.close()

# (a) Count characters, words and lines
lines = text.splitlines()
words = text.split()

print("Total characters:", len(text))
print("Total words:", len(words))
print("Total lines:", len(lines))

# (b) Frequency of each character
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character frequency:")
print(freq)

# (c) Print words in reverse order
print("Words in reverse order:")
print(" ".join(words[::-1]))

# (d) Copy even lines to File1 and odd lines to File2
f1 = open("File1.txt", "w")
f2 = open("File2.txt", "w")

for i in range(len(lines)):
    if (i + 1) % 2 == 0:
        f1.write(lines[i] + "\n")
    else:
        f2.write(lines[i] + "\n")

f1.close()
f2.close()

print("Even lines copied to File1.txt")
print("Odd lines copied to File2.txt")
```

### Sample Input

Contents of `data.txt`:

```text
Hello Python
OOP practical
File handling
```

### Sample Output

```text
Total characters: 40
Total words: 6
Total lines: 3
Character frequency:
{'H': 1, 'e': 2, 'l': 5, 'o': 2, ' ': 3, 'P': 2, 'y': 1, 't': 2, 'h': 2, 'n': 3, '\n': 2, 'O': 2, 'p': 1, 'r': 1, 'a': 3, 'c': 2, 'i': 3, 'F': 1, 'd': 1, 'g': 1}
Words in reverse order:
handling File practical OOP Python Hello
Even lines copied to File1.txt
Odd lines copied to File2.txt
```

### Output Screenshot
<img width="1665" height="192" alt="image" src="https://github.com/user-attachments/assets/8c7b5948-0ac0-409a-9c41-c80a982c326c" />

---

## Practical 10: Dictionary of cubes

**Aim:**  Write a function that prints a dictionary where the keys are numbers between 1 and 5 and the 
values are cubes of the keys.

### Source Code

```python

def cube_dictionary():
    cubes = {}
    n = int(input("How many numbers do you want to enter? "))

    for i in range(1, n + 1):
        num = int(input(f"Enter number {i}: "))
        cubes[num] = num ** 3

    return cubes


result = cube_dictionary()
print("Dictionary of cubes:", result)

```

### Sample Test

```text
How many numbers do you want to enter? 7
Enter number 1: 12
Enter number 2: 23
Enter number 3: 34
Enter number 4: 54
Enter number 5: 657
Enter number 6: 5
Enter number 7: 757
Dictionary of cubes: {12: 1728, 23: 12167, 34: 39304, 54: 157464, 657: 283593393, 5: 125, 757: 433798093}
```

### Output Screenshot

<img width="1167" height="202" alt="image" src="https://github.com/user-attachments/assets/037b2283-5cbc-438d-a0c4-b54ff675bfe0" />


---

## Practical 11: Tuple Operations

**Aim:** Split a tuple into halves, select even values, concatenate tuples, and find maximum and minimum values.

### Source Code

```python

t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. Print half the values in two lines
print("First half:", t1[:5])
print("Second half:", t1[5:])

# b. Print even numbers from the tuple
even = tuple(x for x in t1 if x % 2 == 0)
print("Even numbers:", even)

# c. Concatenate t2 with t1
t2 = (11, 13, 15)
t3 = t1 + t2
print("Concatenated tuple:", t3)

# d. Find maximum and minimum values
print("Maximum value:", max(t1))
print("Minimum value:", min(t1))

```

### Sample Test

```text
First half: (1, 2, 5, 7, 9)
Second half: (2, 4, 6, 8, 10)
Even numbers: (2, 2, 4, 6, 8, 10)
Concatenated tuple: (1, 2, 5, 7, 9, 2, 4, 6, 8, 10, 11, 13, 15)
Maximum value: 10
Minimum value: 1
```

### Output Screenshot

<img width="826" height="130" alt="image" src="https://github.com/user-attachments/assets/c1fe2975-cf53-42e5-ad16-52eca1850da5" />


---

## Practical 12: Employee Class

**Aim:** Create an `Employee` class with employee details, salary calculation, object counting, and formatted output.

### Source Code

```python

class Employee:
    count = 0

    def __init__(self, emp_no, name, dept, basic, da, hra):
        if basic < 0 or da < 0 or hra < 0:
            raise SystemExit(
                "Error: Basic, DA and HRA cannot be negative."
            )

        self.emp_no = emp_no
        self.name = name
        self.dept = dept
        self.basic = basic
        self.da = da
        self.hra = hra

        Employee.count += 1

    def salary(self):
        return self.basic + self.da + self.hra

    def __del__(self):
        if hasattr(self, "emp_no"):
            Employee.count -= 1
            del self.emp_no

    def __str__(self):
        return (
            f"\nEmployee Number: {self.emp_no}\n"
            f"Name: {self.name}\n"
            f"Department: {self.dept}\n"
            f"Basic: {self.basic}\n"
            f"DA: {self.da}\n"
            f"HRA: {self.hra}\n"
            f"Total Salary: {self.salary()}"
        )


try:
    emp_no = int(input("Enter employee number: "))
    name = input("Enter employee name: ")
    dept = input("Enter department: ")
    basic = float(input("Enter basic salary: "))
    da = float(input("Enter DA: "))
    hra = float(input("Enter HRA: "))

    emp = Employee(emp_no, name, dept, basic, da, hra)

    print(emp)
    print("\nNumber of employees:", Employee.count)

except ValueError:
    print("Error: Enter valid numeric values for salary and employee number.")


```

### Sample Test

```text
Enter employee number: 100
Enter employee name: Amit
Enter department: IT
Enter basic salary: 95000
Enter DA: 5000
Enter HRA: 3000

Employee Number: 100
Name: Amit
Department: IT
Basic: 95000.0
DA: 5000.0
HRA: 3000.0
Total Salary: 103000.0

Number of employees: 1
```

### Output Screenshot
<img width="567" height="327" alt="image" src="https://github.com/user-attachments/assets/d281a5dc-56b2-4ecb-a6c7-e537c828aab3" />


---

## Practical 13: 2D Point Class

**Aim:** Define a 2D point class and calculate the distance between two point objects.

### Source Code

```python

import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        d = math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
        return d

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


# Taking input from the user
x1 = float(input("Enter x coordinate of first point: "))
y1 = float(input("Enter y coordinate of first point: "))

x2 = float(input("Enter x coordinate of second point: "))
y2 = float(input("Enter y coordinate of second point: "))

# Creating point objects
p1 = Point2D(x1, y1)
p2 = Point2D(x2, y2)

# Displaying points
print("First point:", p1)
print("Second point:", p2)

# Calculating distance
print("Distance between points:", p1.distance(p2))
)
```

### Sample Test

```text
Enter x coordinate of first point: 12
Enter y coordinate of first point: 30
Enter x coordinate of second point: -20
Enter y coordinate of second point: -40
First point: (12.0, 30.0)
Second point: (-20.0, -40.0)
Distance between points: 76.96752561957543
```

### Output Screenshot

<img width="737" height="160" alt="image" src="https://github.com/user-attachments/assets/4b0dcba3-b992-4327-9484-260b1e9958ca" />


---

## Practical 14: 3D Point Inheritance

**Aim:** Inherit the 2D point class to create a 3D point class and override the distance method.

### Source Code

```python

import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 +
                         (self.y - p.y)**2)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    # Overriding distance method
    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 +
                         (self.y - p.y)**2 +
                         (self.z - p.z)**2)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"


# Taking input from the user
x1 = float(input("Enter x coordinate of first point: "))
y1 = float(input("Enter y coordinate of first point: "))
z1 = float(input("Enter z coordinate of first point: "))

x2 = float(input("Enter x coordinate of second point: "))
y2 = float(input("Enter y coordinate of second point: "))
z2 = float(input("Enter z coordinate of second point: "))

# Creating objects
p1 = Point3D(x1, y1, z1)
p2 = Point3D(x2, y2, z2)

# Displaying points
print("First point:", p1)
print("Second point:", p2)

# Calculating distance
print("Distance between points:", p1.distance(p2))

```

### Sample Test

```text
Enter x coordinate of first point: 12
Enter y coordinate of first point: -24
Enter z coordinate of first point: 12
Enter x coordinate of second point: -24
Enter y coordinate of second point: 12
Enter z coordinate of second point: -24
First point: (12.0, -24.0, 12.0)
Second point: (-24.0, 12.0, -24.0)
Distance between points: 62.353829072479584
```

### Output Screenshot

<img width="621" height="197" alt="image" src="https://github.com/user-attachments/assets/0675929c-3b76-4002-bfee-dc5ce7160c16" />


---

## Practical 15: Name Validation Using Exceptions

**Aim:** Accept a name and raise and handle exceptions if the input contains digits or special characters. Spaces between names are allowed.

### Source Code

```python
def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty")

    if not all(part.isalpha() for part in name.split()):
        raise ValueError(
            "Name must contain only letters and spaces"
        )

    return name

try:
    name = input("Enter your name: ")
    print("Valid name:", validate_name(name))
except ValueError as e:
    print("Invalid name:", e)
```

### Sample Test

```text
Enter your name: khushal
Valid name: khushal
```text
Enter your name: khushal@123
Invalid name: Name must contain only letters and spaces
```


### Output Screenshot
<img width="272" height="42" alt="image" src="https://github.com/user-attachments/assets/afdb5c89-2709-48a7-b134-59481a6ad980" />
<img width="716" height="42" alt="image" src="https://github.com/user-attachments/assets/e345c02d-9e11-43b9-a611-cdb8356f48fa" />


---

## Practical 16: Simple Calculator

**Aim:** Perform addition, subtraction, multiplication, and division.

### Source Code

```python
print("Welcome to the Simple Calculator!")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION") 
print("4. DIVISION")
print("5. EXIT")
choice = input("Enter your choice (1-5): ")

if choice == '1':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print(f"The result of addition is: {result}")

elif choice == '2':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print(f"The result of subtraction is: {result}")

elif choice == '3':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print(f"The result of multiplication is: {result}")

elif choice == '4':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")

elif choice == '5':
    print("Exiting the program.")
else:
    print("Invalid choice. Please enter a number between 1 and 5.")
    
```

### Sample Test

```text
Welcome to the Simple Calculator!
1. ADDITION
2. SUBTRACTION
3. MULTIPLICATION
4. DIVISION
5. EXIT
Enter your choice (1-5): 4
Enter first number: 950
Enter second number: 250
The result of division is: 3.8
```

### Output Screenshot

<img width="566" height="222" alt="image" src="https://github.com/user-attachments/assets/4a32b728-d44f-49bf-8887-60386492d175" />


---


## 🎯 Learning Outcomes

- Understand Python basics, loops, conditions, and functions.
- Perform operations on strings and collections.
- Work with files and dictionaries.
- Understand classes, objects, inheritance, and method overriding.
- Calculate distances using mathematical formulas.
- Handle invalid input with exceptions.
- Develop a simple calculator using conditional statements.

## 👨‍💻 Author
khushal khadiya

Created as part of the **Object Oriented Programming using Python** practical coursework.

---

⭐ If you find this repository useful, consider giving it a star!

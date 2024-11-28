```python
#比较运算符：==,!=,<,>,<=,>=
x = 5
y = 10
#Check if x is equal to y
result = x == y
print(result)
```

    False
    


```python
#Check if x is not equal to y
result2 = x != y
print(result2)
```

    True
    


```python
#Check if x is less than y
result3 = x < y
print(result3)
```

    True
    


```python
#Check if x is greater than y
result4 = x > y
print(result4)
```

    False
    


```python
# 逻辑运算符
# and, or, not
is_sunny = True
is_warm = False
# Check if it is either sunny and warm, 两者满足一个则为假
result5 = is_sunny and is_warm
print(result5)
```

    False
    


```python
# Check if it is either sunny or warm, 二者满足一个则为真
# F + F = F
# F + T = T
# T + F = T
# T + T = T
result6 = is_sunny or is_warm
print(result6)
```

    True
    


```python
# Negate the value of is_sunny
# F → T
# T → F
result7 = not is_sunny
print(result7)
```

    False
    


```python
temperature = 26
is_raining = True
# Check the temperature is between 25 and 30 degrees Celsius and it is not raining
result8 = not is_raining and 25 <= temperature <= 30
print(result8)
```

    False
    


```python
# Conditional Statement
x = 4
if x%2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")
```

    4 is even
    


```python
# Input the values
num1 = 10
num2 = 10
# Do calculations, Give conditions
if num1 < num2:
    # Give the result
    print("Inside if condition")
elif num1 == num2:
    print("num1=num2")
else:
    print("Outside else")
```


```python
# Q1: Write a program that checks if a given number is positive or not
number = 6
if number > 0:
    print(f"{number} is positive")
```

    6 is positive
    


```python
# Q2: Check a given character is a vowel
char = "A"
if char.lower() in "aeiou":
    print(f"{char} is a vowel")
else:
    print(f"{char} is not a vowel")
```

    A is a vowel
    


```python
# Q3 checks if a given year is a leap year
year = 2025
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

    2025 is not a leap year
    


```python
# Q4 takes two numbers prints which one is greater
a = 10
b = 15
if a>b:
    print(f"{a} is greater than {b}")
elif a==b:
    print(f"{a} is equal to {b}")
else:
    print(f"{b} is greater than {a}")
```

    15 is greater than 10
    


```python
# Q5 check if a given number is even or odd
num = int(input("Enter a number: "))
if num%2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
```

    6 is an even number
    


```python
# Q6 check if a given number is a palindrome(回文)
text = "radar"
if text == text[::-1]:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")
```

    radar is a palindrome
    


```python
# Q7 Grades correspond to scores
score = 85
if score>=90:
    print("Grade A")
elif score>=80:
    print("Grade B")
elif score>=70:
    print("Grade C")
elif score>=60:
    print("Grade D")
else:
    print("Grade E")
```


```python
# Q8 Calculate Delta
import cmath

a = 24
b = 32
c = 48

discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    root1=(-b + discriminant ** 0.5) / (2 * a)
    root2=(-b - discriminant ** 0.5) / (2 * a)
    print(f"Roots are real and different: {root1}, {root2}")
elif discriminant == 0:
    root = (-b + discriminant ** 0.5) / (2 * a)
    print(f"Roots are real and the same: {root}")
else:
    root1 = (-b - discriminant ** 0.5) / (2 * a)
    root2 = (-b + discriminant ** 0.5) / (2 * a)
    print(f"Roots are complex: {root1}, {root2}")
```

    Roots are complex: (-0.6666666666666669-1.247219128924647j), (-0.6666666666666666+1.247219128924647j)
    


```python
#Check if a string only certain digests.
```

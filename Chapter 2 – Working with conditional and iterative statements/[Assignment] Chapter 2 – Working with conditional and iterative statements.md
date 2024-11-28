# Chapter 2 Assignment 1

## If else

1. Write a program that checks if a given date (day, month , year)is a valid date, according to a leap year.


```python
date="2024-03-2"
M_D=[("01","31"),("02","29"),("03","31"),("04","30"),("05","31"),("06","30"),("07","31"),("08","31"),("09","30"),("10","31"),("11","30"),("12","31")]
#根据给定日期分割数据
YYYY,MM,DD=date.split("-")
#当公历年份不是整百数时，只看年份数的末两位数，是不是4的倍数，如果年份数末两位是4的倍数，这一年就是闰年。当公历年份是整百数时，只看年份数的千位与百位这两位数，如果这两位数是4的倍数，这一年就是闰年，反之，就是平年。
if (int(YYYY)%100 != 0 and int(YYYY[2:4])%4 == 0) or (int(YYYY)%100 == 0 and int(YYYY[0:2])%4 == 0):
    #检测数据是否一直不合格
    count=0
    for i in range(len(M_D)):
        #检测月份是否正常
        if int(MM)>12:
            print("invalid date!")
        #检测日期是否与月份对应
        elif MM==M_D[i][0] and DD<=M_D[i][1]:
            print("valid date!")
            count+=1
    if count==0:
        print("invalid date!")
else:
    print("The year is not leap year!")
```

    valid date!
    

2. write a program to Find the largest of the four  given number.  


```python
#设定给定数据
nums=[1,2,3,4]
#输出最大的一个
print(max(nums))
```

    4
    

3. Write a program that check if a given number (sum of cubes of it's digit is equal to the number itself)


```python
num=19
str_num=str(num)
list_nums=[]
#创建一个函数，处理后续列表
def cube(x):
    return(int(x)**3)
#将每一数位加入list_nums
for i in range(len(str(num))):
    list_nums.append(str_num[i])
#将每一数位乘方，获得一个新的列表
int_list_cube_nums=list(map(cube,list_nums))
#列表相加比对
if sum(int_list_cube_nums)==num:
    print(f"The sum of the cubes of the digits of {num} is equal to the number itself. ")
else:
    print(f"The sum of the cubes of the digits of {num} isn't equal to the number itself.")
```

    The sum of the cubes of the digits of 19 isn't equal to the number itself.
    

4. Write a program that takes two number and an operator (+ , -, *, /) as input and peforms the specified operation. Handle division by zero errors gracefully. 


```python
#设定两个数字,nums[0]在运算符左边,nums[1]在运算符右边
num1=int(input("请输入第一个数\n"))
num2=int(input("请输入第二个数\n"))
nums=[num1,num2]
method=input("请输入运算符(+ , -, *, /)\n")
#+
if method=="+":
    print(f"{nums[0]} + {nums[1]} = {nums[0]+nums[1]}")
#-
if method=="-":
    print(f"{nums[0]} - {nums[1]} = {nums[0]-nums[1]}")
#*
if method=="*":
    print(f"{nums[0]} * {nums[1]} = {nums[0]*nums[1]}")
#/
if method=="/":
    if nums[1] != 0:
        print(f"{nums[0]} / {nums[1]} = {nums[0]/nums[1]}")
    else:
        print(f"{nums[1]} cannot be used as a divisor")
```

    10 + 20 = 30
    

5. Write a program that checks if a given email addresss is in a valid format (contains "@" and ".")


```python
email="1234@qq.com"
if "@" in email and "." in email:
    print(f"{email} is in a valid format")
else:
    print(f"{email} isn't in a valid format")
```

    1234@qq.com is in a valid format
    

6. Write a program that simulates a game of rock , paper , scissor and determine the winner. 


```python
#所有可能的选择
choose=["R","P","S"]
win_choose=["P","S","R"]
#你做出的选择
your_choose=input("请输入你的选择\n")
#第二个人做出的选择
other_choose=input("请输入对方的选择\n")
if your_choose == other_choose:
    #平局
    print("A Draw")
#如果对方的选择等于自己的选择对应的win列表里的选择，就输了
elif other_choose==win_choose[choose.index(your_choose)]:
    print("You Lose!")
else:
    print("You Win!")
```

    You Lose!
    

# while loop 

7. Write a program that prints numbers from 1 to 10 using a while loop.


```python
i=0
while i != 10:
    i+=1
    print(i)
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    

8. Create a program that calculates the sum of all numbers from 1 to n, where n is provided by the user.


```python
n=5
i=0
sum=0
while i!=n:
    i+=1
    sum+=i
print(sum)
```

    15
    

9. Write a program to find the factorial of a given number using a while loop.


```python
#给定数字
n=5
#零
sum=1
while n!=1:
    sum*=n
    n-=1
print(sum)
```

    120
    

10. Create a program that reverses the digits of a given number using a while loop.


```python
num=123456789
str_num=str(num)
i=1
rev_num=""
while i != len(str_num)+1:
    rev_num+=str_num[-i]
    i+=1
print(rev_num)
```

    987654321
    

11. Write a program to print the Fibonacci sequence up to a given number n using a while loop.


```python
a=1
b=1
n=5
list=[a,b]
while i !=n:
    list.append(a+b)
    if a+b>=n:
        break
    a=list[-2]
    b=list[-1]
print(f"{list}")

```

    [1, 1, 2, 3, 5]
    

12. Write a program that checks if a given number is a happy number (repeatedly replace the numberwith the sum of the squares of it's digit until it becomes 1 or loops endlessly. 


```python
#给定一个数字
num=3
#数据处理
str_num=str(num)
while True:
    #检测数字是否变为1
    if int(str(num)[-1]) == 1:
        break
    else:
       #检测数字是否无限循环
       print(str_num[-len(str(int(str_num[-1])**2)):])
       print(str(int(str_num[-1])**2))
       if str_num[-len(str(int(str_num[-1])**2)):]==str(int(str_num[-1])**2):
           print(str_num)
           break
       else:
            str_num.rstrip(str(str_num)[-1])
            str_num+=str(int(str(str_num)[-1])**2)
            print(str_num)
print(f"{num} is a happy number")
```

    3
    9
    39
    39
    81
    3981
    1
    1
    3981
    3 is a happy number
    

# For loop 

13. Write a program that prints all even numbers from 1 to 20 using a for loop.


```python
for i in range(2,21,2):
    print(i)
```

    2
    4
    6
    8
    10
    12
    14
    16
    18
    20
    

14. Create a program that calculates the sum of all elements in a given list using a for loop.


```python
list=[1,2,3,4,5,6,7,8,9]
sum=0
for i in range(len(list)):
    sum+=list[i]
print(sum)
```

    45
    

15. Write a program that counts the number of vowels in a given string using a for loop.


```python
string="The quick brown fox jumps over the lazy dog"
count=0
for i in range(len(string)):
    if string[i] in "aeiou":
        count+=1
print(count)
```

    11
    

16. Create a program that finds the largest number in a given list using a for loop.


```python
list=[1,2,3,4,5,6,7,8,9]
for i in range(len(list)):
    #骑驴找驴
    if list[i]==max(list):
        print(f"{list[i]} is the largest number in list")
        break
```

    9 is the largest number in list
    

17. Write a program that prints the multiplication table of a given number using a for loop.


```python
for i in range(1,10):
    for u in range(1,10):
        if u<9:
            print(f"{i} * {u} = {i*u}",end=" ")
        else:
            #只是为了好看
            print(f"{i} * {u} = {i*u}",end="\n")
```

    1 * 1 = 1 1 * 2 = 2 1 * 3 = 3 1 * 4 = 4 1 * 5 = 5 1 * 6 = 6 1 * 7 = 7 1 * 8 = 8 1 * 9 = 9
    2 * 1 = 2 2 * 2 = 4 2 * 3 = 6 2 * 4 = 8 2 * 5 = 10 2 * 6 = 12 2 * 7 = 14 2 * 8 = 16 2 * 9 = 18
    3 * 1 = 3 3 * 2 = 6 3 * 3 = 9 3 * 4 = 12 3 * 5 = 15 3 * 6 = 18 3 * 7 = 21 3 * 8 = 24 3 * 9 = 27
    4 * 1 = 4 4 * 2 = 8 4 * 3 = 12 4 * 4 = 16 4 * 5 = 20 4 * 6 = 24 4 * 7 = 28 4 * 8 = 32 4 * 9 = 36
    5 * 1 = 5 5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25 5 * 6 = 30 5 * 7 = 35 5 * 8 = 40 5 * 9 = 45
    6 * 1 = 6 6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36 6 * 7 = 42 6 * 8 = 48 6 * 9 = 54
    7 * 1 = 7 7 * 2 = 14 7 * 3 = 21 7 * 4 = 28 7 * 5 = 35 7 * 6 = 42 7 * 7 = 49 7 * 8 = 56 7 * 9 = 63
    8 * 1 = 8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64 8 * 9 = 72
    9 * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81
    

# Continue statement 

18. Write a program to print all the odd numbers from 1 to 10. Use the continue statement to skip even numbers.


```python
for i in range(11):
    if i%2==0:
        print(i)
    else:
        continue
```

    0
    2
    4
    6
    8
    10
    

19. Create a program that takes a list of names and prints each name unless it starts with the letter "A". Use continue to skip names starting with "A".


```python
list=["Abandon","aobama","cliff","bilibili"]
for i in range(len(list)):
    if list[i][0]== "A" or list[i][0]== "a":
        continue
    else:
        print(list[i])
```

    cliff
    bilibili
    

20. Write a program to display all numbers from 1 to 50 except for multiples of 5. Use the continue statement to skip such numbers.


```python
for i in range(51):
    if i%5!=0:
        print(i)
    else:
        continue
```

    1
    2
    3
    4
    6
    7
    8
    9
    11
    12
    13
    14
    16
    17
    18
    19
    21
    22
    23
    24
    26
    27
    28
    29
    31
    32
    33
    34
    36
    37
    38
    39
    41
    42
    43
    44
    46
    47
    48
    49
    

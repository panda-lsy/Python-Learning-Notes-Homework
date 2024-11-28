#### 1. Write a Python function to find the Max of three numbers.


```python
def max_(a,b,c):
    list_=[a,b,c]
    for num in list_:
        if num>=a and num>=b and num>=c:
            return num
a,b,c=4,5,6
print(max_(a,b,c))
```

    6
    

#### 2. Write a Python function to sum all the numbers in a list.

Sample List : (8, 2, 3, 0, 7)

Expected Output : 20


```python
def sum_(list_):
    op=0
    for i in list_:
        op+=i
    return op
sum_([8,2,3,0,7])
```




    20



#### 3. Write a Python program to reverse a string.

Sample String : "1234abcd"

Expected Output : "dcba4321"



```python
def palindrome(string):
    str_list=[]
    for i in range(len(string),0,-1):
        str_list.append(string[i-1])
    op=''.join(str_list)
    return op
palindrome("1234abcd")
```




    'dcba4321'



#### 4. Write a Python function to check whether a number is in a given range.
请输入range_,格式为(a,b)


```python
def checkrange(n,range_):
    if n in eval(range_):   #将字符串转换为一个范围
        print(f"{n} is in range")
    else:
        print(f"{n} is not in range")
    return
n=int(input("Enter a number: \n"))
range_=input("Enter a range: [Expected input:(a,b)]")
checkrange(n,range_)
```

    6 is not in range
    

#### 5. Write a Python function that accepts a string and calculate the number of upper-case letters and lower case letters.

Sample String : 'The quick Brow Fox'

Expected Output :

No. of Upper case characters : 3

No. of Lower case Characters : 12



```python
def check_up_and_low(string):
    upper=0
    lower=0
    for character in string:
        if character.isupper():
            upper+=1
        elif character.islower():
            lower+=1
        else:
            continue
    print(f"No. of Upper case characters : {upper}\nNo. of Lower case characters : {lower}")
string="The quick Brow Fox"
check_up_and_low(string)
            
```

    No. of Upper case characters : 3
    No. of Lower case characters : 12
    

#### 6. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.



```python
input_num=int(input("Enter a number: \n"))
add_15 = lambda input_num: input_num+15
x=int(input("Enter a number X: \n"))
y=int(input("Enter a number Y: \n"))
multiply= lambda x,y: x*y
print(add_15(input_num))
print(multiply(x,y))
```

    18
    20
    

#### 7. Write a Python program to sort a list of tuples using Lambda.


```python
tup=("Amy","Bat","QQ","Cat")
a=lambda tup:sorted(list(tup))
print(a(tup))
```

    ['Amy', 'Bat', 'Cat', 'QQ']
    

#### 8. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.


```python
def multiple_with_an_unknown_num(x):
    unknown_num=5
    return x*unknown_num
x=int(input("Enter a number: \n"))
multiple_with_an_unknown_num(x)
```




    15



#### 9. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. Sample Items : green-red-yellow-black-white Expected Result : black-green-red-white-yellow 


```python
def sort_input_str(string):
    list_=list(string.split('-'))
    ans='-'.join(sorted(list_))
    return ans
sort_input_str('green-red-yellow-black-white')
```




    'black-green-red-white-yellow'



#### 10. Write a Python program to create Fibonacci series upto n using Lambda. 


```python
n=int(input("Enter a number: \n"))
if n<=1:
    print(1,1)
else:
    print(1,1,end=' ')
    fibonacci=lambda a=1,b=1,n=100: (print(a+b,end=' '),fibonacci(b,a+b,n)) if a+b<=n else print("\n")
    fibonacci(n=n)
```

    1 1 2 3 5 8 13 21 34 55 89 
    
    

#### 11. Write a Python program to count the even, odd numbers in a given array of integers using Lambda. 


```python
num=int(input("Enter a number: \n"))
check_even_or_odd=lambda num: print('Even') if num%2==0 else 'Odd'
check_even_or_odd(num)
```

    Even
    

#### 12. Write a Python program to square and cube every number in a given list of integers using Lambda.


```python
list_=[1,2,3,4,5]
square=list(map(lambda x:x**2,list_))
cube=list(map(lambda x:x**3,list_))
print(square)
print(cube)
```

    [1, 4, 9, 16, 25]
    [1, 8, 27, 64, 125]
    

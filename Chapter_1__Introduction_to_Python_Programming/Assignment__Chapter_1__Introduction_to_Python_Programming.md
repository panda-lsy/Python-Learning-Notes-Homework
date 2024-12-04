##### Declare a value x and assign it the value 10. Print the value of X


```python
# Program
# Declare a value x
x = 10
# Print the value of X
print(x)
```

    10


##### Declare two variable a and b , assign then the values 5 and 3 and swap their values without using a third variable


```python
# Program
# Declare two variable a and b
a = 5
b = 3
print(a)
print(b)
# swap their values
a, b = b, a
print(a)
print(b)
```

    5
    3
    3
    5


##### Assign the values of 25. 5 to variable priceand print it's type


```python
# Program
# Assign the values of 25. 5 to variable
price = 25.5
# print it's type
print(type(price))
```

    <class 'float'>


##### Create a variable name and assign your full name to it, Then printa greeting message that says : "Hello , [Your name]!"


```python
# Program
# Create a variable name
name = "LiuShunyao"
# print a greeting message
print("Hello,", name)
```

    Hello, LiuShunyao


##### Assign a string to a variable sentence split into a list of words and print the list


```python
# Program
# Assign a string to a variable sentence
sentence = "The quick brown fox jumps over a lazy dog"
# split into a list of words 
sentence = sentence.split(' ')
# print the list
print(sentence)
```

    ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'a', 'lazy', 'dog']


# DataType 

##### Create a variable num with the value 100, and check if it is of type integer.


```python
# Program
# Create a variable num
num = 100
# Check if it is of type integer
Is_Type_Int = type(num) == int
print(Is_Type_Int)
```

    True


##### Convert the integer 100 to a string and concatenate it with another string "Apples".Print the result.


```python
# Program
# Convert the integer 100 to a string
num = 100
num = str(num)
# concatenate it with another string "Apples"
result = num + "Apples"
# Print the result.
print(result)
```

    100Apples


##### declare a tuple with teh value (10, 20, 30, 40). try to change the first value and explain the error


```python
# Program
# declare a tuple
tup = (10, 20, 30, 40)
# try to change the first value
try:
    tup[0] = 11
# explain the error
except Exception as error:
    print(error)
```

    'tuple' object does not support item assignment


##### Create a dictionary with keys , name and age and assign appropriate values to them. Print the value associated with age key 


```python
# Program
# Create a dictionary with keys
dictionary = dict(name="Liu",age="18")
#Print the value associated with age key
print(dictionary["age"])
```

    18


##### Create a variable x with a value of 25.convert this value into a float, a string and a boolean and print the type of each conversion 


```python
# Program
# Create a variable x with a value of 25.
x = 25
#convert this value
x_float = float(x)
x_string = str(x)
x_boolean = bool(x)
#print the type of each conversion 
print(type(x_float))
print(type(x_string))
print(type(x_boolean))
```

    <class 'float'>
    <class 'str'>
    <class 'bool'>



```python
# Program

```


```python
# Program

```


```python
# Program

```


```python
# Program

```

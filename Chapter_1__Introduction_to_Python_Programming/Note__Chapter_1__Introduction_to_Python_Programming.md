# Python语言介绍


```python
# Program
#Input
a = 2
b = 3

#Calculation
c = a+b

#Result Display
print(c)
```

    5
    


```python
# Program
print("Welcome to Python Programming")
```

    Welcome to Python Programming
    


```python
# Program
a = 5
print(type(a))
```

    <class 'int'>
    


```python
# Program
a= 5.001
b=float(a)
print(b)
print(type(b))

#j是虚数单位
c= 3 + 3j
print(type(c))

d = "Liu" #变量名只能用字母/下划线开头
print(type(d)) 

_d = 3 #变量名不能用数字开头，可以在
```

    5.001
    <class 'float'>
    (3+3j)
    


```python
# Program
fruits = ["apple", "pear", "orange", "banana"]
print(fruits)
print(type(fruits))
print(fruits[0])
```

    ['apple', 'pear', 'orange', 'banana']
    <class 'list'>
    apple
    


```python
# Program
number = (10, 20, 30, 40, 50, 60) #元组数据不可改变
print(number)
print(type(number))
#number[0] = 22 如果强行修改会报错
```

    (10, 20, 30, 40, 50, 60)
    <class 'tuple'>
    


```python
# Program
number_range = range(1,11)
print(list(number_range))
print(str(number_range)) #可以把函数形式转化为字符
print(type(number_range))
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    range(1, 11)
    <class 'range'>
    


```python
# Program
a = 10
print(type(a))
b = list(str(a))
print(type(b))
c = float(a)
print(c)
```

    <class 'int'>
    <class 'list'>
    10.0
    


```python
# Program
# Dictionary (Mappings) 字典映射
person = dict(name="Liu", age=20, city="San Francisco") #Tab补全的另外一种表示方法,将dict文字转换为dict构造函数
print(person)           # 输出整个字典
print(person["name"])   # 输出字典的一个特定数据
'''
person = {                  #教授的方法
    "name": "Liu",
    "age": 20,
    "city": "San Francisco"
}
'''
person["name"] = "Liu-is"
print(person)
```

    {'name': 'Liu', 'age': 20, 'city': 'San Francisco'}
    Liu
    {'name': 'Liu-is', 'age': 20, 'city': 'San Francisco'}
    


```python
# Program
#布尔类型
x = 5
y = 10
is_greater = x > y
print(is_greater)

is_equal = x == y
print(is_equal)
```

    False
    False
    


```python
# Program
#集合
fruits_1 = {"apple", "pear", "orange", "barnana"}
print(fruits_1)
fruits_1 = {"apple", "pear", "orange", "banana","banana"}
print(fruits_1) #会自动合并重复元素
fruits_1.add("lemon")   #添加元素
print(fruits_1)
fruits_1.remove("banana")   #删除元素
print(fruits_1)
```

    {'orange', 'apple', 'pear', 'banana'}
    {'orange', 'apple', 'pear', 'banana'}
    {'pear', 'apple', 'lemon', 'orange', 'banana'}
    {'pear', 'apple', 'lemon', 'orange'}
    

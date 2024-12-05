# Python 编程介绍
Python 是一种解释型语言，在程序开发过程中可以节省大量时间，因为无需编译和链接。因为无需编译和链接。解释器可以交互式使用，这使得语言的功能进行实验，编写一次性程序，或在自下而上的程序开发过程中测试功能。自下而上的程序开发过程中测试功能。它还是一个方便的桌面计算器。

## Python 的特点
Python 提供了许多有用的功能，这些功能使它与其他编程语言相比更受欢迎、更有价值。它支持面向对象编程、过程式编程方法，并提供动态内存分配。  
下面列出了一些基本功能：

### 可移植性(Portability)

Python 可以在任何地方运行，将程序从 Linux 移植到 Windows 或 Mac 通常只需要路径和设置。  
Python 是为可移植性而设计的，它能照顾到操作系统 (OS)，这就省去了我们为特定平台编写代码的工作。

### 内容丰富的库文件(An extensive library)

Python 有一个非常广泛的标准库。全世界的 Python 社区维护着大量的 第三方库，人们可以在 Python 包索引(PyPI)。  
当我们编写 Python 代码并意识到需要某种功能时，在大多数情况下，至少有一个库已经为我们实现了该功能。

### 面向对象的语言(Object-oriented language)

Python 支持面向对象的语言，并出现了类和对象的概念。 它支持继承、多态和封装等。 面向对象的程序有助于程序员编写可重复使用的代码，用更少的代码开发应用程序。

### 可嵌入(Embeddable)
其他编程语言的代码可以在 Python 源代码中使用。我们也可以在其他编程语言中使用 Python 源代码。它可以将其他语言嵌入到我们的代码中。

### 动态类型(Dynamic typed)

在 Python 中，我们不需要指定变量的数据类型。当我们给变量赋值时，它会在运行时自动为变量分配内存。假设我们给 `x` 赋了整数值 `15`，那么我们不需要写  
```cpp
int x = 15
```
只需写入 `x = 15` 即可。

### 解释型语言(Interpreted language)

Python 是一种解释型语言，因为 Python 代码是逐行执行的。C、C++、Java 等语言一样，Python 代码不需要编译，这使得调试代码更加容易。python 的源代码会被转换成一种叫做字节码的直接形式。


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


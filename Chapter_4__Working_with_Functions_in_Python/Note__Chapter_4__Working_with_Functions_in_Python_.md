## 函数 
### 定义  
函数是一个有组织、可重复使用的代码块，用于执行单个相关操作。函数为应用程序提供了更好的模块化和更高的代码重用率。
函数块以关键字 `def` 开头，后跟函数名和括号 ( ( ) )
`def function_name(parameters):`


```python
# Program
def print_me(string):
    print(string)
    return
print_me("Hello World")
```

    Hello World



```python
# Program
def add(a,b):
    c=a+b
    return c
add(3,4)
```




    7



创建一个change_List函数，将mylist追加一个值


```python
# Program

```


```python
# Program
def change_list(mylist):
    mylist.append([1,2,3])
    print("Values inside the function",mylist)
    return
mylist=[1,2,3]
change_list(mylist)
print("Values outside the function",mylist)
```


```python
# Program
def modify(x):
    x =15
    print(x,id(x))
    return x
x =3
modify(5)
print(x,id(x))
```

    15 140705720499064
    3 140705720498680



```python
# Program
def add_num(a,b):
    c=a+b
    return c
add_num(3,4)
```




    7




```python
# Program
def check_even_or_odd(num):
    if num%2==0:
        ans="Even"
    else:
        ans="Odd"
    return ans
check_even_or_odd(5)
```




    'Odd'




```python
# Program
def check_prime(num):
    if num<=1:
        ans="Prime"
    for i in range(2,num):
        if i != num-1:
            if num%i==0:
                ans="Not prime"
                break
        else:
            ans="Prime"
            break
    return ans
check_prime(5)

```




    'Prime'




```python
# Program
def print_factorial(num):
    ans=1
    for i in range(1,num+1):
        ans*=i
    return ans
print_factorial(5)
```




    120



## 形参`Parameter（Param）`和实参`Argument（Arg）`的区别  
定义函数 `def add(a,b)`时，a,b为实参  
调用函数 `add(3,4)`时，3,4为实参  
## 关键字参数  
关键字参数是通过参数名进行传递的参数，它们不依赖于参数的位置。  
可以在函数调用时指定参数名，这样参数的顺序可以与函数定义中的顺序不一致，不会引发错误。  
使用关键字参数可以提高代码的可读性，并且使得函数调用更加清晰和明确。  
## 位置参数  
位置参数是函数定义中按照顺序声明的参数，调用函数时必须按照相同的顺序传递参数。  
参数的位置和数量必须与函数定义中的位置参数相匹配，否则会引发错误。  
位置参数传递的方式是根据参数在函数定义中的位置来匹配参数值。 
## ! 若在定义函数给参数提前赋值(默认值)，即使不调用参数也可以运行。 
## *不定长参数
定义一个不定长位置参数 *args，它可以接受任意数量的位置参数。在函数体内，通过循环遍历 args 元组，将所有参数相加并返回结果。



```python
# Program
def grocery(item,price):
    print('Item = %s' %item)
    print('Price = %s' %price)
grocery(price=5,item="apple")   #关键字参数调用
grocery("banana",35)    #位置参数
```

    Item = apple
    Price = 5



```python
# Program
def plus(*args):    #不定长参数
    a=0
    for i in args:
        a+=i
    return a
plus(1,2,3,4,5)
```




    15




```python
# Program
def cauculator_(cau_type,*args):
    if cau_type=='add':
        return sum(args)
    if cau_type=='multiply':
        ans=1
        for i in args:
            ans*=i
        return ans
    if cau_type=='subtract':
        ans=args[0]
        for i in args:
            if i == args[0]:
                continue
            else:
                ans-=i
        return ans
    if cau_type=='divide':
        ans=args[0]
        for i in args:
            if i == args[0]:
                continue
            if i == 0:
                print(f"{ans} cannot be divided by i.")
            else:
                ans/=i
        return ans
cauculator_('subtract',3,4,5)
            
        
```




    -6



## 内置函数  
### 绝对值 `abs()`
### 二进制 `bin()`
### 累加 `sum()`
### 将特殊符号转换成二进制 `ascii()`
### 获取字符串长度`len()`
### 将变量转换为本地变量`locals()`或全局变量`global()`
global单独输出会作为字典


```python
# Program

```


```python
# Program

```

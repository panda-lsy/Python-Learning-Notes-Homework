# 实用库(Libraries)
## Operating System(OS) Interface
### 介绍
Python OS系统模块为建立用户与操作系统之间的交互提供了便利。  
它提供了许多有用的操作系统函数，用于执行基于操作系统的任务和获取操作系统的相关信息。  
OS隶属于 Python 的标准库实用程序模块。该模块提供了一种可移植的方式来使用依赖于操作系统的功能。
### 使用
通过导入模块`import os`

### os.name
该函数给出所导入的操作系统相关模块的名称。目前已注册的名称有：“posix”、“nt”、“os2”、“ce”、“java ”和 “riscos”。


```python
# Program
import os

print(os.name)
```

    nt
    

### 功能
#### 查看当前文件目录 `os.getcwd()`  
通过`os.getcwd()`  
函数`os.getcwd()` 返回用于执行代码的文件的当前工作目录 *（Current Working Directory）*


```python
# Program
original_path = os.getcwd()     #记录初始工作目录,用于后续还原路径
print(os.getcwd())
```

    E:\PythonProgramming\Python-Learning-Notes-and-Homework\Python-Learning-Notes-Homework\Chapter 5 – Use of Standard Library
    

#### 新建文件夹 `os.mkdir()`  
通过`os.mkdir()`,创建新的目录


```python
# Program
os.mkdir("D:\\Demo")    #它将根据函数字符串参数中的路径，在 D 盘中创建名为 Demo 文件夹的新目录。
```

#### 更改到其他工作目录 `os.chdir()`  
方法 `chdir()` 将当前工作目录更改为给定路径。它在所有情况下都返回 None。  
要将当前目录设置为父目录，请在 `chdir()` 函数中使用“.. ”作为参数。


```python
# Program
os.chdir("D://")   
#检查当前工作目录
retval=os.getcwd() 
print("Directory changed successfully",retval)
```

    Directory changed successfully D:\
    


```python
# Program
 # 新建文件夹
os.mkdir("D://Tempdir") 
# 修改当前工作目录
os.chdir("D://Tempdir")   
# 检测当前工作目录
retval=os.getcwd() 
print("Directory changed successfully",retval) 
os.chdir("..") 
# 获得当前目录（为所在目录的父目录）
retval=os.getcwd() 
print("Parent directory is",retval) 
```

    Directory changed successfully D:\Tempdir
    Parent directory is D:\
    

#### 删除工作目录 `os.rmdir()`
OS模块中的 `rmdir()` 函数可以删除指定目录的绝对路径或相对路径。  
但是，我们不能删除 **当前工作目录(被占用)**。  
此外，要删除的目录 **必须是空目录**。   
例如，如果 `tempdir` 是当前目录，就不会被移除。我们必须更改当前工作目录，然后删除 `tempdir`。


```python
# Program
#错误示范
os.chdir("D://tempdir") 
#check current working directory 
print(os.getcwd()) 
#remove current working directory 
os.rmdir("D://tempdir")
```

    D:\tempdir
    


    ---------------------------------------------------------------------------

    PermissionError                           Traceback (most recent call last)

    Cell In[6], line 6
          4 print(os.getcwd()) 
          5 #remove current working directory 
    ----> 6 os.rmdir("D://tempdir")
    

    PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问。: 'D://tempdir'


这将导致 **权限错误** *(另一个程序正在使用此文件，进程无法访问)*。这就是我们必须更改当前工作目录的原因。


```python
# Program
#正确示范
os.chdir("D://tempdir") 
os.chdir("..")      #切换到父目录
os.rmdir("tempdir") 
```

### 辅助功能
内置的 `dir()` 和 `help()` 函数可作为处理 os 等大型模块的交互式辅助工具：  
`dir(os)`返回所有模块函数的列表   
`help(os)`返回根据模块文档字符串创建的详细手册页面 


```python
# Program
print(dir(os)) 
print(help(os)) 
```

## 获取需求文件
### Glob模块
glob 模块可查找与指定模式匹配的所有路径名。它提供了一个从目录通配符搜索中生成文件列表的函数


```python
# Program
import glob 
os.chdir(original_path)
retvalue=glob.glob("*.ipynb") 
print(retvalue) 
```

    ['[Note] Chapter 5 – Use of Standard Library.ipynb']
    

## sys模块
Python 的 `sys.argv` 属性是一个保存命令行参数的列表，它可以让我们在运行 Python 程序时直接将参数传入，并且可以通过修改这个列表来控制程序的行为。   
这些参数以列表形式存储在 `sys` 模块的 `argv` 属性中，Python sys 模块通过 `sys.argv` 提供对任何命令行参数的访问。
- sys.argv 是命令行参数列表。
- len(sys.argv) 是命令行参数的个数 
### 使用效果：
新建一个python(.py)文件,并写入以下内容:  
```
import sys  
print("命令行参数有：", str(sys.argv))    
for i in range(len(sys.argv)):  
    print("第", i, "个参数：", sys.argv[i])
```    
保存，并打开命令行，找到python文件所在路径并输入以下内容:  
`python XXX.py Hello`  
效果会如下:  
```
命令行参数有： ['test_4_sys.py', 'hello']  
第 0 个参数： test_4_sys.py  
第 1 个参数： hello  
```
### 范例
在本笔记的父文件夹中有`test_4_sys.py`，可以试运行。




```python
# Program
import sys   
print(sys.argv) 
print(type(sys.argv)) 
print(len(sys.argv)) 

```

    ['E:\\PythonProgramming\\Python-Learning-Notes-and-Homework\\.venv\\Lib\\site-packages\\ipykernel_launcher.py', '-f', 'C:\\Users\\33223\\AppData\\Roaming\\jupyter\\runtime\\kernel-ce52df91-c498-48d6-b483-22836cd1c4f1.json']
    <class 'list'>
    3
    

## 数学运算
Python math 模块定义了最著名的数学函数，包括三角函数、表示函数、对数函数等。  
### 数学常数
π（pi）：它是一个著名的数学常数，定义为圆周率与圆直径之比。其值为 3.141592653589793。  
自然常数（e）： 它被定义为自然对数的底数，其值为 2.718281828459045。  



```python
# Program
import math
print(math.pi)
print(math.e)
```

    3.141592653589793
    2.718281828459045
    

### 取对数
#### 以e为底  
`math.log(数字,底数)`此方法返回给定数字的自然对数，如果不填底数，默认为`e`


```python
# Program
import math 
number=2e-7 
print('log(fabs(x), base) is',math.log(math.fabs(number),10))   #math.fabs()取绝对值
```

    log(fabs(x), base) is -6.698970004336019
    

#### 以10为底
`math.log10() `
此方法返回给定数字的 10 为底对数，称为标准对数。


```python
# Program
x=13 # small value of of x     
print('log10(x) is :', math.log10(x))     
```

    log10(x) is : 1.1139433523068367
    

### 返回浮点数
`math.exp()` 返回该数值以e为幂的结果


```python
# Program
number = 1  # small value of of x     
print('The given number (x) is :', number)     
print('e^x (using exp() function) is :', math.exp(number))  
```

    The given number (x) is : 1
    e^x (using exp() function) is : 2.718281828459045
    

### 向下取整
`math.floor(x)` 此方法返回 x 的底限值。它返回小于或等于 x 的值。


```python
# Program
number = math.floor(10.25201)  
print("The floor value is:",number)   
```

    The floor value is: 10
    



### 向上取整
`math.ceil(x) `此方法返回 x 的ceil 值。它返回大于或等于 x 的值。



```python
# Program
number = math.ceil(10.25201)  
print("The ceil value is:",number)  
```

    The ceil value is: 11
    

### 阶乘运算
math.factorial() 此方法返回给定数字 x 的阶乘。如果 x 不是整数，会引发 ValueError。


```python
# Program
number = math.factorial(7)   
print("The factorial of number:",number)  
```

    The factorial of number: 5040
    

### 幂运算
`math.pow(x,y)` 此方法返回与 y 值对应的 x 的幂。如果 x 的值为负数或 y 不是整数，则会引发 ValueError。


```python
# Program
number = math.pow(10,2)   
print("The power of number:",number)  
```

    The power of number: 100.0
    

## Random 随机库
Random模块提供了进行随机选择的工具：  
`random.choice()` 随机选择列表的元素
`random.sample()` 不放回取样  
`random.random()` 随机浮点数(默认在[0,1]之间选择)  
`random.randrange()` 抽取范围中的一个整数



```python
# Program
import random 
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10)) # sampling without replacement 
print(random.random()) # random float 
print(random.randrange(6)) # random integer chosen from range(6) 
```

    banana
    [23, 77, 16, 57, 75, 17, 67, 6, 72, 89]
    0.4897683840477597
    5
    

## 数据统计
统计模块计算数值数据的基本统计属性（平均值、中位数、方差等）
`statistics.mean()`返回一个数集的算数平均值  
`statistics.median()`返回一个数集的中位数  
`statistics.variance()`返回一个数集的方差


```python
# Program
import statistics 
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5] 
print(statistics.mean(data))  
print(statistics.median(data))
print(statistics.variance(data))
```

    1.6071428571428572
    1.25
    1.3720238095238095
    

## 日期时间
Python 提供的 datetime 模块可以处理真实的日期和时间。  
在实际应用中，我们需要处理日期和时间,Python 使我们能够安排我们的 Python 脚本在特定的时间运行。   
### time模块
在 Python 中，日期不是一种数据类型，但我们可以通过导入以 datetime、time 和 calendar 命名的模块来处理日期对象。  
通过`import time` 导入

#### 获取时间戳
>时间戳，是从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数（不考虑闰秒），用于表示一个时间点。然而，这种格式对于人类阅读并不友好，因此需要转换成可读的日期和时间格式。这个工具能够将时间戳快速转换为人类可读的日期时间格式，同时也支持反向转换，即将日期时间转换为时间戳。
> 
通过`print(time.time())`打印自 1970 年 1 月 1 日上午 12 点以来的时间戳  


```python
# Program
import time  
#prints the number of ticks spent since 12 AM, 1st January 1970   
print(time.time())   
```

    1732152892.721108
    

#### 获取当前时间
time模块的 `localtime()` 函数用于获取当前时间元组。请看下面的示例。


```python
# Program
print(time.localtime(time.time()))
```

    time.struct_time(tm_year=2024, tm_mon=11, tm_mday=21, tm_hour=12, tm_min=46, tm_sec=46, tm_wday=3, tm_yday=326, tm_isdst=0)
    

#### 获取格式化时间
使用time模块的 `asctime()` 函数可以格式化时间。它会返回所传递时间元组的格式化时间。


```python
# Program
print(time.asctime(time.localtime(time.time())))   
```

    Thu Nov 21 09:36:21 2024
    

### Datetime模块
 datetime 模块使我们能够创建自定义日期对象，对日期执行各种操作，如比较等。要以日期对象的形式处理日期，我们必须在 python 源代码中导入 datetime 模块。  
 请看下面的示例，以获取当前时间的 datetime 对象表示法。


```python
# Program
import datetime   
#returns the current datetime object      
print(datetime.datetime.now()) 
```

### Calendar模块
Python 的calendar模块提供了一个日历对象，该对象包含各种用于处理日历的方法。请看下面的示例，以打印 2020 年 7月 的日历。


```python
# Program
import calendar    
cal = calendar.month(2020,7)     
#printing the calendar of December 2018     
print(cal)
```

         July 2020
    Mo Tu We Th Fr Sa Su
           1  2  3  4  5
     6  7  8  9 10 11 12
    13 14 15 16 17 18 19
    20 21 22 23 24 25 26
    27 28 29 30 31
    
    

## 数据压缩
模块直接支持常见的数据归档和压缩格式，包括：zlib、gzip、bz2、lzma、zipfile 和 tarfile。
### 示例
`s`为原始数据  
`t`为通过zlib压缩后的数据  
通过len()可以看出,数据长度减少了。  
通过`zlib.decompress()`来实现压缩数据的解压。  
通过`zlib.crc32()`来获取其循环冗余校验的错误检测码。


```python
# Program
import zlib 
s = b'witch which has which witches wrist watch' 
print(len(s),s) 
t = zlib.compress(s) 
print(len(t),t) 
print(zlib.decompress(t))
print(zlib.crc32(s))
```

    41 b'witch which has which witches wrist watch'
    37 b'x\x9c+\xcf,I\xceP(\xcf\xc8\x04\x92\x19\x89\xc5PV9H4\x15\xc8+\xca,.Q(O\x04\xf2\x00D?\x0f\x89'
    b'witch which has which witches wrist watch'
    226805979
    

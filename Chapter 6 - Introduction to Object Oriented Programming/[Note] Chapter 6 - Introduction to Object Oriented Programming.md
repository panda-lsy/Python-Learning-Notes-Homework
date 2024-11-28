# 面向对象编程
>面向对象程序设计是种具有对象概念的程序编程典范，同时也是一种程序开发的抽象方针。它可能包含数据、属性、代码与方法。对象则指的是类的实例。它将对象作为程序的基本单元，将程序和数据封装其中，以提高软件的重用性、灵活性和扩展性，对象里的程序可以访问及经常修改对象相关联的数据。在面向对象程序编程里，计算机程序会被设计成彼此相关的对象。
## 主要概念
- **类(Class)**: 用来描述具有相同的属性和方法的对象的集合，类是对象的蓝图或模板。它定义了一类对象共有的属性和行为。
- **类变量(Class Variable)**：类变量在整个实例化的对象中是公用的。类变量是属于类本身的变量，而不是特定于某个对象的变量。
- **实例变量 (Instance Variable)**：实例变量是属于对象的变量，它们存储在对象内部，并且每个对象都有自己独立的一份。
- **对象(Object)**：对象是类的实例。每个对象都是根据类的定义创建出来的，并且拥有自己的状态（即实例变量）。
- **方法 (Method)**：方法是定义在类中的函数，用于操作类或对象的属性。

## 实例与讲解
我们创建了一个记录教学对象的信息系统，定义了`T_and_S`类。  
其中:  
- `total_count`就是类变量，他记录了教学对象的总人数。  
- `def __init__`在类中定义的函数为方法，其中`__init__`类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法。实参应该使用小写。  
  - 在类中，`self.Name` 为实例变量 
  - `@classmethod` 为类方法，它使用 `@classmethod` 装饰器，可以通过类本身调用，也可以通过对象调用。
- 通过对变量赋值类名加括号，内置属性，来创建不同的对象
- 通过`对象.实例变量`来访问对象属性
- 类变量`total_count`的值将在这个类的所有实例之间共享，在内部类或外部类使用 `T_and_S.total_count` 访问


```python
class T_and_S:  #创建了一个T_and_S的类
    """记录老师和同学的信息"""    #类文档字符串
    #类变量
    total_count=0
    
    def __init__(self, name, age, role):   #方法（Method）
        #实例变量
        self.Name = name
        self.Age = age
        self.Role = role
        # 每次创建一个新的对象时，总人数增加1
        T_and_S.total_count+=1
        
    #类方法 
    @classmethod
    def get_total_count(cls):
        return cls.total_count
    
#通过类创建不同对象
Leo = T_and_S('Leo', 18, "Student")
Sakura = T_and_S('Sakura', 22, "Student")
Kshitij = T_and_S('Kshitij', 23, "Teacher")

#访问属性
print("There are {} People".format(T_and_S.total_count))
print("{} is a {} year old {}".format(Leo.Name, Leo.Age, Leo.Role))
```

    There are 3 People
    Leo is a 18 year old Student
    

## 编写 Python 类并使用对象

### 创建类(Class)
请看下面的示例，创建的 Employee 类包含两个字段，分别是 Employee id和姓名这两个字段。  
该类还包含一个函数 display()，用于显示 Employee 的信息。


```python
class Employee:
    id = 10
    name = "Sam"
    def display(self):
        print(self.name, self.id)
        
emp = Employee()
emp.display()
```

    Sam 10
    

### 创建类的实例
下面的示例创建了上例中定义的 Employee 类的实例。  
其中,通过占位符来代替变量：  
`%s`来替换字符串变量  
`%d`来替换数字变量  
通过转义字符来换行:  
`\n`来换行


```python
class Employee:     
    id = 10    
    name = "Sam"     
    def display (self):     
        print("ID: %d \nName: %s"%(self.id,self.name))     
    #Creating a emp instance of Employee class   
    emp = Employee()     
    emp.display()
```

    ID: 10 
    Name: Sam
    

### 构造函数
构造函数(`__init__`)是一种特殊的方法，用于初始化类的实例成员。  
它接收`self`作为第一个关键字  
有两种种类：
- 参数化构造函数
- 非参数化构造函数  
以下分别为两种例子：


```python
class Employee:
    count=0
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        Employee.count+=1
    
    def display(self):
        print("ID: %d \nName: %s"%(self.id,self.name))
        print("There are {} employees".format(self.count))
        
emp1 = Employee(1, "Sam")
emp2 = Employee(2, "Amy")
Employee.display(emp1)
```

    ID: 1 
    Name: Sam
    There are 2 employees
    


```python
class Employee:
    def __init__(self):
        print("这是非参数化构造函数")
    
    def display(self,name):
        print("Hello",name)

emp1=Employee()
emp1.display("Hans")
```

    这是非参数化构造函数
    Hello Hans
    

#### 构造函数的更多细节
##### Python 默认构造函数
当我们没有在类中包含构造函数或忘记声明构造函数时，该构造函数就会成为默认的构造函数。  
它不执行任何任务，只是初始化对象。 请看下面的例子。


```python
class Employee:     
    id = 10    
    name = "Sam"     
    def display (self):     
        print("ID: %d \nName: %s"%(self.id,self.name))     
    #Creating a emp instance of Employee class   
    emp = Employee()     
    emp.display()
```

##### 多个构造函数
只会生效后面的一个，前面的会被覆盖掉。


```python
class Student:   
    def __init__(self):   
        print("The First Constructor")   
    def __init__(self):   
        print("The second contructor")   
st = Student()  
```

    The second contructor
    


### 方法与函数、类和类的实例的区分
类的方法与函数有一个区别，前者有一个**额外的第一个参数**名称`self`  
而`self`指向的是类和地址，而`self.__class__`指向类。


```python
class Test:
    def show(self):
        print(self)
        print(self.__class__)

t = Test()
t.show()
```

    <__main__.Test object at 0x000001EA4779BEF0>
    <class '__main__.Test'>
    

### 删除实例变量
通过`del 对象.实例变量()`来删除其实例变量.  
在删除后会报错`AttributeError: 'Employee' object has no attribute 'id'`


```python
del emp.id
emp.display()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[15], line 1
    ----> 1 del emp.id
          2 try:
          3     print(1)
    

    AttributeError: 'Employee' object has no attribute 'id'


### 生成一个对象
设置一个变量等于类名加括号,可以通过type()检查变量类型。


```python
class Test:
    pass
Obj = Test()
type(Obj)
```




    __main__.Test





## 内置类函数(Built-in class functions)
下表介绍了该类中定义的内置函数。
|S.N| Function| Description |  
| ---------- | ----------- |  ----------- |  
|1 |getattr(obj,name,default) |用于访问对象的属性 |
|2 |setattr(obj,name,value)| 用于为对象的特定属性设置特定值. |
|3 |delattr(obj,name) |用于删除特定属性. |
|4 |hasattr(obj,name) |如果对象包含某些特定属性，则返回 true. |


```python
class Student: 
    def __init__(self, name, id, age): 
        self.name = name 
        self.id = id 
        self.age = age 
# 创建Student类对象   
s = Student("John", 101, 22) 
# 打印对象 s 的属性名称  
print(getattr(s, 'name')) 
# 将属性 age 的值重置为 23
setattr(s, "age", 23) 
# 打印 age 的修改值
print(getattr(s, 'age')) 
# 如果学生包含名称为 id 的属性，则打印为 True
print(hasattr(s, 'id')) 
# 删除 age 属性 
delattr(s, 'age') 
# 这将导致错误，因为属性 age 已被删除
print(s.age) 
```

    John
    23
    True
    


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[27], line 19
         17 delattr(s, 'age') 
         18 # 这将导致错误，因为属性 age 已被删除
    ---> 19 print(s.age) 
    

    AttributeError: 'Student' object has no attribute 'age'


### 内置类属性(Built-in class attributes)
除了其他属性，Python 类还包含一些内置的类属性，这些属性提供了关于类的信息。  
下表给出了内置类属性。
|S.N| Function| Description |  
| ---------- | ----------- |  ----------- |  
|1 |`__dict__` |它提供了包含类命名空间的信息|
|2 |`__doc__`| 它包含一个字符串，该字符串的类为文档 |
|3 |`__name__`|用于访问类名. |
|4 |`__module__`|它用于访问其中类的模块 |
|5 |`__bases__`|它包含一个元组，其中包括所有基类 |


```python
class Student:  
    '这是关于类的文档'
    def __init__(self,name,id,age):     
        self.name = name
        self.id = id  
        self.age = age     
    def display_details(self):     
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))     
s = Student("John",101,22)     
print(s.__dict__)   
print(s.__doc__)     
print(s.__module__)   
```

    {'name': 'John', 'id': 101, 'age': 22}
    这是关于类的文档
    __main__
    

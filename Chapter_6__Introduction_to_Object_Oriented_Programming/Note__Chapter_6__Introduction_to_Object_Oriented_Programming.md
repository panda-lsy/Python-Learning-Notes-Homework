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
# Program
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
# Program
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
# Program
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
# Program
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
# Program
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
# Program
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
# Program
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
# Program
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
# Program
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
# Program
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
# Program
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
# Program
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


## `Self`的使用
在面向对象编程中，每当我们为一个类定义方法时，我们都会使用 self 作为第一个参数。 让我们看看一个名为 Cat 的类的定义。


```python
# Program
class Cat: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    def info(self): 
        print(f"I am a cat.My name is {self.name}.I am {self.age} years old.") 
    def make_sound(self): 
        print("Meow")
```

在这种情况下，包括 `__init__` 在内的所有方法的第一个参数都是 self。  
我们知道，类是对象的蓝图, 这个蓝图可以用来创建多个对象。   
让我们用上面的类创建两个不同的对象。


```python
# Program
cat1 = Cat('Andy',2)
cat1.info()
cat1.make_sound()
```

    I am a cat.My name is Andy.I am 2 years old.
    Meow


self 关键字用于表示给定类的实例（对象）。 在本例中，两个猫对象 cat1 和 cat2 有自己的名称和年龄属性。  
如果没有 self 参数，同一个类就无法保存这两个对象的信息。  
但是，由于类只是一个蓝图，self 允许访问每个对象的属性和方法。这使得每个对象都有自己的属性和方法。 因此，创建在定义类时，我们就引用了 self 作为对象。

### 为什么每次都要明确定义self?
Python 禅宗所说：

>"显式比隐式好"。

那么，我们为什么要这样做呢？  
让我们先举一个简单的例子，我们有一个 Point 类，它定义了一个用于计算与原点距离的方法 distance。


```python
# Program
class Point(object): 
    def __init__(self,x = 0,y = 0): 
        self.x = x 
        self.y = y 
    def distance(self): 
        """Find distance from origin""" 
        return (self.x**2 + self.y**2) ** 0.5

p1=Point(6,8)
p1.distance()
```




    10.0



在上例中，`__init__()` 定义了三个参数，但我们只传入了两个（6 和 8）。  
同样distance() 需要一个参数，但我们只传入了零个参数。  
为什么 Python 没有报错参数不匹配？

### 原理
上述示例中的 Point.distance 和 p1.distance 并不完全相同。


```python
# Program
print(type(Point.distance))
print(type(p1.distance))
```

    <class 'function'>
    <class 'method'>


我们可以看到，第一个是函数(Function)，第二个是方法(Method)。  
正如 *###方法与函数、类和类的实例的区分* 所说，  

>类的方法与函数有一个区别，前者有一个**额外的第一个参数**名称`self`  

方法的一个特殊之处是，对象本身会作为第一个参数传递给相应函数的第一个参数。  
在上述示例中，方法调用 `p1.distance()` 实际上等同于`Point.distance(p1)`。  
一般来说，当我们调用一个带有参数的方法时，相应的类函数会被调用，方法的对象会被放在第一个参数之前。  
将方法对象放在第一个参数之前。 因此，类似 `obj.meth(args)` 这样的函数会变成 `Class.meth(obj, args)`。  
调用过程是自动的，而接收过程则不是。

### 规避`self`隐式行为
现在你已经清楚，对象（实例）本身会自动作为第一个参数传递。在创建静态方法时，可以避免这种隐式行为。  
请看下面这个简单的例子：


```python
# Program
class A(object): 
    @staticmethod 
    def stat_meth(): 
        print("Look no self was passed") 
```

在这里，`@staticmethod` 是一个函数装饰器，它使 `stat_meth()` 成为静态。 让我们实例化这个类并调用该方法。


```python
# Program
a=A()
a.stat_meth()
print(type(A.stat_meth))
print(type(a.stat_meth))
```

    Look no self was passed
    <class 'function'>
    <class 'function'>


## 多个实例
到目前为止，我们已经定义了一个类，构建了一个对象，使用了该对象.  
然而，在面向对象编程中，当我们为我们的类构造多个实例时，才真正体现了它的威力。  
当我们用类构造多个对象时，我们可能想为每个对象设置不同的初始值。  
我们可以向构造函数传递数据，为每个对象设置不同的初始值：  


```python
# Program
class PartyAnimal: 
    x = 0 
    name = '' 
    def __init__(self, nam): 
        self.name = nam 
        print(self.name,'constructed') 
    def party(self) : 
        self.x = self.x + 1 
        print(self.name,'party count',self.x) 
s = PartyAnimal('Sally') 
j = PartyAnimal('Jim') 
s.party() 
j.party() 
s.party() 
```

    Sally constructed
    Jim constructed
    Sally party count 1
    Jim party count 1
    Sally party count 2


构造函数有一个指向对象实例的自参数和一些附加参数，这些参数会在对象构造过程中传递给构造函数：  
`s = PartyAnimal('Sally') `  
在构造函数中，第二行复制了传入 name 属性的参数 (nam):  
`self.name = nam `
程序的输出显示，每个对象（s 和 j）都包含各自独立的 x 副本和 nam 的独立副本。


## 类的继承
继承是面向对象范例的一个重要方面，继承为程序提供了代码重用性，因为我们可以使用已有的类来创建新的类，而不是从头开始创建。  
因为我们可以使用现有的类来创建一个新类，而不是从头开始创建。在继承过程中，子类获得属性，并能访问父类中定义的所有数据成员和函数，子类还可以为父类的函数提供特定的实现。
在 Python 中，派生类或子类可以继承基类或父类，只需在派生类名称后的括号中提及基类或父类。   
将基类继承到派生类的语法如下：  
```
class derived-class(base class):   
    <class-suite> 
```
一个类可以继承多个类，只需在括号内提及所有类即可。 


```python
# Program
class Animal:  #父类
    def speak(self):   
        print("Animal Speaking") 
#子类 Dog 继承了基类 Animal
class Dog(Animal):   
    def bark(self):   
        print("dog barking")   
d = Dog()   
d.bark()   
d.speak()
```

    dog barking
    Animal Speaking


我们将创建一个新程序，并从 `__init__()` 构造函数方法开始，我们将为每个 Fish 对象或子类填充 name_name 和 last_name 类变量。


```python
# Program
class Fish: 
    def __init__(self, first_name, last_name="Fish"): 
        self.first_name = first_name 
        self.last_name = last_name 
    def swim(self): 
        print("The fish is swimming.") 
    def swim_backwards(self): 
        print("The fish can swim backwards.")
```

我们用字符串 "Fish "初始化了我们的姓氏变量，因为我们知道大多数鱼的姓氏都是 "fish"。   
我们在 Fish 类中添加了 `swim()` 和 `swim_backwards()` 方法，这样每个子类都可以使用这些方法。  
让我们为它创建一个子类.对于子类，我们可以选择添加更多方法、覆盖现有的父类方法，或者直接接受默认的父类方法：


```python
# Program
class Trout(Fish): 
    pass 
terry = Trout("Terry") 
print(terry.first_name + " " + terry.last_name) 
terry.swim() 
terry.swim_backwards() 
```

    Terry Fish
    The fish is swimming.
    The fish can swim backwards.


我们创建了一个 Trout 对象 `terry`，它使用了 `Fish` 类的每个方法，尽管我们没有在 `Trout` 子类中定义这些方法。  
我们没有在 Trout 子类中定义这些方法。 我们只需将 "Terry" 的值传递给 `first_name` 变量的值，因为所有其他变量都已初始化。

接下来，让我们创建另一个包含自己方法的子类。  
我们称这个类为 `Clownfish` ，它的特殊方法将允许它与海葵一起生活：


```python
# Program
class Clownfish(Fish): 
    def live_with_anemone(self): 
        print("The clownfish is coexisting with sea anemone.")
casey = Clownfish("Casey") 
print(casey.first_name + " " + casey.last_name) 
casey.swim() 
casey.live_with_anemone()
```

    Casey Fish
    The fish is swimming.
    The clownfish is coexisting with sea anemone.


输出结果显示，小丑鱼对象 `casey` 能够使用鱼类方法 `__init__()` 和 `swim()` 以及它的子类方法 `live_with_anemone()`。

## 重写父方法
到目前为止，我们已经研究了子类 Trout以及另一个子类 Clownfish，它继承了父类的所有行为，后者创建了子类特有的方法。  
但有时，我们会希望使用父类的某些行为，而不是全部。  
当我们更改父类方法时我们会覆盖它们。  
在构建父类和子类时，必须牢记程序设计，以便覆盖不会产生不必要或多余的代码。

我们将为 Fish 父类创建一个 Shark 子类。 有鉴于此，我们将覆盖 `__init__()` 构造函数方法和 `swim_backwards()` 方法。  
我们不需要修改 swim() 方法，因为鲨鱼是会游泳的鱼类。


```python
# Program
class Shark(Fish): 
    def __init__(self, first_name, last_name="Shark"): 
        self.first_name = first_name 
        self.last_name = last_name 
    def swim_backwards(self): 
        print("The shark cannot swim backwards, but can sink backwards.") 
```

我们重载了 `__init__()` 方法中的初始化参数，因此 `last_name` 变量现在被设置为等于字符串 "Shark".  
类的每个实例也可以重写这些参数。
`swim_backwards()` 方法现在打印的字符串与父类 Fish 中的字符串不同。  
现在我们可以创建一个 Shark 子类的实例，该实例仍将使用方法：


```python
# Program
sammy = Shark("Sammy") 
print(sammy.first_name + " " + sammy.last_name) 
sammy.swim()#super class method 
sammy.swim_backwards() 
```

    Sammy Shark
    The fish is swimming.
    The shark cannot swim backwards, but can sink backwards.


鲨鱼子类成功覆盖了鱼类的 `__init__()` 和 `swim_backwards()` 方法，同时也继承了父类的 `swim()` 方法。

## `super()`
使用 `super()` 函数，可以访问类中已被覆盖的继承方法对象。
当我们使用 `super()` 函数时，我们是将父方法调用到子方法中来使用它。例如，我们可能想覆盖父方法的某方面功能，但随后调用原始父方法的其余部分来完成该方法。
`super()` 函数最常用于 `__init__()` 方法，因为您将在这里最有可能需要为子类添加一些唯一性，然后从父类完成初始化。

让我们修改一下 `Trout` 子类，看看它是如何工作的。 由于鳟鱼是典型的淡水鱼，我们在 `__init__()` 方法中添加一个`water` 变量，并将其设置为等于字符串 "freshwater"，然后保持其余的的变量和参数：


```python
# Program
class Trout(Fish): 
    def __init__(self, water = "freshwater"): 
        self.water = water 
        super().__init__(self)
```

由于我们重载了该方法，因此不再需要将 `first_name` 作为参数传递给 `Trout`的参数，而如果我们确实传递了参数，我们将重置 `freshwater`。 因此，我们将初始化
name 变量进行初始化。


```python
# Program
terry = Trout() 
# Initialize first name 
terry.first_name = "Terry" 
# Use parent __init__() through super() 
print(terry.first_name + " " + terry.last_name) 
# Use child __init__() override 
print(terry.water) 
# Use parent swim() method 
terry.swim() 
```

    Terry Fish
    freshwater
    The fish is swimming.


输出结果显示，Trout 子类的对象 terry 既能使用子类特有的`__init__()` 变量 water，同时还能调用 Fish 父类的 `__init__()` 变量 first_name、last_name变量。  
Python 内置函数 super() 使我们在重写父类方法时也能使用父类方法。

## Python 多级继承
与其他面向对象语言一样，Python 也可以实现多级继承。  
多级继承是当一个派生类继承另一个派生类时，就会产生多级继承。  
在 python 中，多级继承的级数没有限制。
语法：
```
class class1:   
<class-suite>    
class class2(class1):   
<class suite>   
class class3(class2):   
<class suite>
```


```python
# Program
class Animal:   
    def speak(self):   
        print("Animal Speaking")   
#The child class Dog inherits the base class Animal   
class Dog(Animal):   
    def bark(self):   
        print("dog barking")   
#The child class Dogchild inherits another child class Dog   
class DogChild(Dog):   
    def eat(self):   
        print("Eating bread...")   
d = DogChild()   
d.bark()   
d.speak()   
d.eat() 
```

    dog barking
    Animal Speaking
    Eating bread...


## issubclass(sub, sup) 方法
`issubclass(sub, sup)` 方法用于检查指定类之间的关系。 它如果第一个类是第二个类的子类，则返回 `True`，否则返回 `False`。


```python
# Program
class Calculation1:   
    def Summation(self,a,b):   
        return a+b;   
class Calculation2:   
    def Multiplication(self,a,b):   
        return a*b;   
class Derived(Calculation1,Calculation2):   
    def Divide(self,a,b):   
        return a/b;   
d = Derived()   
print(issubclass(Derived,Calculation2))   
print(issubclass(Calculation1,Calculation2)) 
```

    True
    False


## isinstance (obj, class) 方法
`isinstance()` 方法用于检查对象和类之间的关系。 如果第一个参数（即 `obj`）是第二个参数（即 `class`）的实例，则返回 `True`。
示例


```python
# Program
class Calculation1:   
    def Summation(self,a,b):   
        return a+b
class Calculation2:   
    def Multiplication(self,a,b):   
        return a*b
class Derived(Calculation1,Calculation2):   
    def Divide(self,a,b):   
        return a/b
d = Derived()   
print(isinstance(d,Derived)) 
```

    True


## 多态性
多态指的是使用单个类型实体（方法，运算符或对象）来表示不同场景中的不同类型。
在创建类方法时，我们可以使用多态的概念，因为Python允许不同的类具有相同名称的方法。这样，函数就可以使用任何这些多态类的对象，而不需要注意类之间的区别。

鸭子类型是动态类型的一种风格。在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由"当前方法和属性的集合"决定。  
这个概念的名字来源于由*James Whitcomb Riley*提出的鸭子测试。“鸭子测试”可以这样表述：  
“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”



### 创建多态类
为了使用多态性，我们将创建两个不同的类，分别用于两个不同的对象。这两个不同的类都需要有一个共同的接口，这样它们才能被使用。因此，我们将赋予它们不同但名称相同的方法。  
我们将创建一个`Shark`类和一个`Clownfish`类，每个类都将定义 `swim()` 的方法、`swim_backwards()` 和 `skeleton()` 的方法。


```python
# Program
class Shark(): 
    def swim(self): 
        print("The shark is swimming.") 
    def swim_backwards(self): 
        print("The shark cannot swim backwards, but can sink backwards.") 
    def skeleton(self): 
        print("The shark's skeleton is made of cartilage.") 
class Clownfish(): 
    def swim(self): 
        print("The clownfish is swimming.") 
    def swim_backwards(self): 
        print("The clownfish can swim backwards.") 
    def skeleton(self): 
        print("The clownfish's skeleton is made of bone.")
```

在上面的代码中，Shark类和Clownfish类都有三个同名的方法。但是，每个类的这些方法的功能各不相同


```python
# Program
sammy = Shark() 
sammy.skeleton() 
casey = Clownfish() 
casey.skeleton()
```

    The shark's skeleton is made of cartilage.
    The clownfish's skeleton is made of bone.


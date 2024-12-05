### 1. Write a Python program to get the class name of an instance in Python. 
### 1. 编写一个 Python 程序，获取 Python 实例的类名。



```python
# Program
class Example:
	def __init__(self, name, value):
		self.name = name
		self.value = value

example_instance = Example("example", 42)
print(example_instance.__class__.__name__)
```

    Example


### 2. Create a Python class and write a program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once. 
### 2. 创建一个 Python 类并编写一个程序，使用 "a"、"e"、"i"、"o"、"u "创建所有可能的字符串。 请使用这些字符一次。


```python
# Program
class String:
    def __init__(self, args):
        self.chars=args

    def print_all_kinds(self):
        for i in range(len(self.chars)):
            print(''.join(self.chars))
            self.chars.append(self.chars[0])
            self.chars.pop(0)

string = String(['a','e','i','o','u'])
string.print_all_kinds()
        
```

    aeiou
    eioua
    iouae
    ouaei
    uaeio


### 3. Derive class Contact from the base classes Person and Address and use their methods to print out the contact information. 
### 3. 从基类 Person 和 Address 派生出类 Contact，并使用它们的方法来打印联系人信息。

Hint: Address class: show() will print street and city 
提示：Address类：show() 将打印街道和城市信息

Person class: show() will print name and email
Person类：show() 将打印姓名和电子邮件




```python
# Program
class Person:
    def __init__(self, name):
        self.name = name

    def name_show(self):
        print(f'姓名:{self.name}')

class Address:
    def __init__(self, address):
        self.address = address

    def address_show(self):
        print(f"地址:{self.address}")

class Contact(Person, Address):
    def __init__(self, name, address):
        Person.__init__(self, name)
        Address.__init__(self, address)

    def print_information(self):
        self.name_show()
        self.address_show()

example = Contact('name1', 'address1')
example.print_information()


```

    姓名:name1
    地址:address1


### 4. Create a SavingsAccount class that behaves just like a BankAccount, but also has an interest rate and a method that increases the balance by the appropriate amount of interest. 
### 4. 创建一个 SavingsAccount 类，该类的行为与 BankAccount 类似，但也有一个利率和一个按适当利息额增加余额的方法。



```python
# Program
class SavingsAccount:
    def __init__(self, rate, amount, time):
        self.rate=rate
        self.amount=amount
        self.time=time
    
    def amount_cauculation(self):
        print(f'你原来的余额是{self.amount}\n利率为{self.rate}\n{self.time}年后,你的余额为{self.amount*((self.rate+1)**self.time)}')

example = SavingsAccount(0.018,10000,30)
example.amount_cauculation()
```

    你原来的余额是10000
    利率为0.018
    30年后,你的余额为17077.855714711026


### 5. Create a BankAccount class. Your class should support the following methods: 
### 5. 创建一个 BankAccount 类。 您的类应支持以下方法：

```python
# Program
class BankAccount: 
    """Bank Account protected by a pin number.\n银行账户受密码保护""" 

    def __init__(self, pin): 
    """Initial account balance is 0 and pin is 'pin'.\n初始账户余额为 0，密码为 "pin"。""" 

    def deposit(self, pin, amount): 
    """Increment account balance by amount and return new balance.\n按金额增加账户余额并返回新余额。""" 

    def withdraw(self, pin, amount): 
    """Decrement account balance by amount and return amount withdrawn.\n按金额减少账户余额，并退回提取的金额。""" 

    def get_balance(self, pin): 
    """Return account balance.\n退还账户余额。""" 

    def change_pin(self, oldpin, newpin): 
    """Change pin from oldpin to newpin.\n将旧密码改为新密码""" 
    
```

As you implement your BankAccount class, you should think about the following: 

- What should be stored within the BankAccount class? That is, what are its instance variables? 
- What should happen if the wrong pin is provided for any of the methods (other than __init__, which is setting the initial pin)? 
- What should happen if you try to withdraw more than is in the account? 

Does your bank account behave as you expect? Try depositing and/or withdrawing change, instead of whole dollar amounts. Do you want your real bank account to behave this way?

在实现 BankAccount 类时，您应该考虑以下几点：

- BankAccount 类中应存储哪些内容？ 也就是说，它的实例变量是什么？
- 如果为任何方法（除 __init__ 以外，该方法用于设置初始密码）提供了错误的密码，会发生什么情况？
- 如果试图提取的金额超过账户余额，会发生什么情况？

您的银行账户是否如您所料？ 尝试存入和/或取出零钱，而不是整数美元。 您希望您的真实银行账户也这样吗？



```python
# Program
class BankAccount: 
    """Bank Account protected by a pin number.\n银行账户受密码保护""" 

    def __init__(self, pin): 
        """Initial account balance is 0 and pin is 'pin'.\n初始账户余额为 0，密码为 "pin"。""" 
        self.pin=pin
        self.amount=0
        self.login_state=False

    def deposit(self): 
        """Increment account balance by amount and return new balance.\n按金额增加账户余额并返回新余额。""" 
        name='存款系统'
        if self.login_state==False:
            psw=input(f'{name}:请输入密码\n')
            if psw == self.pin:
                print(f'{name}:密码输入正确')
                self.login_state=True
                deposit_amount=float(input(f'{name}:请输入存入金额'))
                if deposit_amount>0:
                    
                    self.amount+=deposit_amount
                    print(f'{name}:已存入{deposit_amount}')
                else:
                    print(f'{name}:不合法数据')
            else:
                print(f'{name}:密码输入错误')

        elif self.login_state==True:
            print(f'{name}:已处于登录(Debug)状态')
            deposit_amount=float(input(f'{name}:请输入存入金额'))
            if deposit_amount>0:
                self.amount+=deposit_amount
                print(f'{name}:已存入{deposit_amount}')
            else:
                print(f'{name}:不合法数据')


    def withdraw(self): 
        """Decrement account balance by amount and return amount withdrawn.\n按金额减少账户余额，并退回提取的金额。""" 
        name='取款系统'
        if self.login_state==False:
            psw=input(f'{name}:请输入密码\n')
            if psw == self.pin:
                print(f'{name}:密码输入正确')
                self.login_state=True
                withdraw_amount=float(input(f'{name}:请输入取出金额'))
                if withdraw_amount>0:
                    if withdraw_amount>self.amount:
                        print(f'{name}:余额不足')
                    else:
                        self.amount-=withdraw_amount
                        print(f'{name}:已取出{withdraw_amount}')
                else:
                    print(f'{name}:不合法数据')
            else:
                print(f'{name}:密码输入错误')

        elif self.login_state==True:
            print(f'{name}:已处于登录(Debug)状态')
            withdraw_amount=float(input(f'{name}:请输入取出金额'))
            if withdraw_amount>0:
                if withdraw_amount>self.amount:
                    print(f'{name}:余额不足')
                else:
                    self.amount-=withdraw_amount
                    print(f'{name}:已取出{withdraw_amount}')
            else:
                print(f'{name}:不合法数据')


    def get_balance(self): 
        """Return account balance.\n查看账户余额。""" 
        name='余额查询'
        if self.login_state==False:
            psw=input(f'{name}:请输入密码\n')
            if psw == self.pin:
                print(f'{name}:密码输入正确')
                self.login_state=True
                self.amount_view='%.2f'%self.amount
                print(f'{name}:账户余额：{self.amount_view}')
            else:
                print(f'{name}:密码输入错误')
        else:
            print(f'{name}:已处于登录(Debug)状态')
            self.amount_view='%.2f'%self.amount
            print(f'{name}:账户余额：{self.amount_view}')

    def change_pin(self): 
        """Change pin from oldpin to newpin.\n将旧密码改为新密码""" 
        name='密码重置'
        oldpin=input(f'{name}:请输入旧密码\n')
        if oldpin == self.pin:
            print(f'{name}:密码输入正确')
            newpin=input(f'{name}:请输入新密码\n')
            self.pin=newpin
            self.login_state=False
        else:
            print(f'{name}:密码输入错误')
        
example = BankAccount('reforge3074')
example.deposit()
example.get_balance()
example.withdraw()
example.get_balance()
example.change_pin()
example.get_balance()
```

    存款系统:密码输入正确
    存款系统:已存入2001.1
    余额查询:已处于登录(Debug)状态
    余额查询:账户余额：2001.10
    取款系统:已处于登录(Debug)状态
    取款系统:已取出1022.3
    余额查询:已处于登录(Debug)状态
    余额查询:账户余额：978.80
    密码重置:密码输入正确
    余额查询:密码输入正确
    余额查询:账户余额：978.80


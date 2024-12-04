#### 1. Write a Python program to multiplies all the items in a list. 


```python
# Program
ans=1
list_=[1,2,3,4,5,6,7,8,9,10]
for num in list_:
    ans*=num
print(ans)
```

    3628800


#### 2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
##### 2. 编写一个 Python 程序，从给定的字符串列表中计算字符串长度为 2 或以上且首尾字符相同的字符串的数量。


```python
# Program
list_=['Good','GG','CATC']
count=0
for string in list_:
    if len(string)>=2 and string[0]==string[-1]:
        count+=1
print(count)
```

    2


#### 3. Write a Python program to create a tuple with different data types. 
##### 3. 编写一个 Python 程序，用不同的数据类型创建一个元组。


```python
# Program
tup=tuple([0,"a",list([1,2]),set([2,3]),dict({"name":"TwentyThree"})])
for element in tup:
    print(type(element))
print(tup)
```

    <class 'int'>
    <class 'str'>
    <class 'list'>
    <class 'set'>
    <class 'dict'>
    (0, 'a', [1, 2], {2, 3}, {'name': 'TwentyThree'})


#### 4. Write a Python program to convert a list to a tuple 


```python
# Program
list_=[1,2,3,4]
print(type(list_))
tup=tuple(list_)
print(type(tup))
```

    <class 'list'>
    <class 'tuple'>


#### 5. Write a Python script to concatenate following dictionaries to create a new one. 
##### 5. 编写一个 Python 脚本，将下列字典连接起来，创建一个新的字典。

Sample Dictionary : 
```
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50, 6:60} 
```

Expected Result : 
```
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
```



```python
# Program
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50, 6:60} 
dic=dict(dic1)
dic.update(dic2)
dic.update(dic3)
print(dic)
```

    {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


#### 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 

Sample Input :  
```
n = 5 
```
Expected Output : 
```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
```


```python
# Program
n = 5
dic=dict()
for i in range(n+1):
    d0={i:i*i}
    dic.update(d0)
print(dic)
```

    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


#### 7. Write a Python program to remove an item from a set if it is present in the set.


```python
# Program
set_={"a","b"}
list_set_=list(set_)
set_.discard(list_set_[-1])
print(set_)
```

    {'b'}


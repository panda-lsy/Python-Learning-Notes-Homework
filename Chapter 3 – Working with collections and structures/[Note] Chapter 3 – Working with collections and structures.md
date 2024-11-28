# List(列表)

## 介绍

list 是 Python 中最通用的数据类型，可以写成一个由逗号分隔的 值（项）的列表。
其中的值不需要相同的数据类型。

## 列表值与数据切割

要访问列表中的值，请使用方括号进行切片，并使用一个或多个索引来获取该索引中的可用值要访问列表中的值，请使用方括号进行切片，并使用一个或多个索引来获取该索引中的可用值  
` List[Start:End:Step] `  
Start:开始的序号  
End:倒数第二个序号,要输出最后一个元素要+1  
Step:每隔(Step-1)个输出  


```python
from soupsieve.css_match import DAYS_IN_WEEK

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]: ", list1[0]) 
print("list1[0:3]: ", list1[0:3]) 
print("list1[0:4:1]: ", list1[0:4:2])
print( "list2[1:5]: ", list2[1:5]) 
print( "list2[-5:-1]: ", list2[-5:-1])#不包括list2[-1]
print( "list2[-5:-1:-1]: ", list2[-1:-5:-1])#回文，不包括list2[-5]
print( "list2[::-1]: ", list2[::-1])#回文
print( "list2[-1]: ", list2[-1])
```

    list1[0]:  physics
    list1[0:3]:  ['physics', 'chemistry', 1997]
    list1[0:4:1]:  ['physics', 1997]
    list2[1:5]:  [2, 3, 4, 5]
    list2[-5:-1]:  [3, 4, 5, 6]
    list2[-5:-1:-1]:  [7, 6, 5, 4]
    list2[::-1]:  [7, 6, 5, 4, 3, 2, 1]
    list2[-1]:  7
    

## 列表赋值  
直接通过中括号赋值即可


```python
list2=[0,1,2]
print(list2[2])
list2[2]=2001
print(list2[2])
```

    2
    2001
    

## 列表添加元素
使用 ` list.append() `


```python
list2.append(3)
print(list2)
```

    [0, 1, 2001, 3]
    

## 列表删除元素
使用 ` del(list[X]) ` 或者 ` list.pop(X) `(X是元素所在的序号,若不填写则为最后一个,若对变量赋值为它,则为最后一个元素) 或者 ` list.remove(element)`(element是元素值)


```python
del(list2[2])
print(list2)
list2.append(4)
list2.pop(-1)
print(list2)
list2.append(4)
list2.remove(4)
```

    [0, 1, 3]
    [0, 1, 3]
    

## 列表获取长度  
使用 ` len(list) `,返回一个int


```python
print(len(list2))
print(type(len(list2)))
```

    3
    <class 'int'>
    

## 列表相加  
使用 ` + `,连接两个列表


```python
list1=[3,4,5]
print(list2+list1)
```

    [0, 1, 3, 3, 4, 5]
    

## 列表元素重复添加 
使用 ` *X `,重复添加元素


```python
list3=["Hi","Hello"]*3
print(list3)

```

    ['Hi', 'Hello', 'Hi', 'Hello', 'Hi', 'Hello']
    

## 列表判断元素是否在列表
使用 ` element in count `,返回一个True/False


```python
print("Hi" in list3)
```

    True
    

## 列表遍历元素的值
使用 ` for element in list:`,第二行缩进,element可以是任意变量名,返回的是遍历的元素值


```python
for element in list3:
    print(element)
```

    Hi
    Hello
    Hi
    Hello
    Hi
    Hello
    

## 列表判断元素出现次数
使用 ` list.count(element) `,查找元素的数量,返回一个int


```python
print(list3)
print(list3.count("Hi"))
```

    ['Hi', 'Hello', 'Hi', 'Hello', 'Hi', 'Hello']
    3
    

## 列表数据反向排序
使用 ` list.reverse() `,返回一个元素排序相反的list  


```python
list3.reverse()
print(list3)
```

    ['Hello', 'Hi', 'Hello', 'Hi', 'Hello', 'Hi']
    

## 获取特定元素
使用 ` max(list) ` 和 `min(list)` 分别获取列表中第一个序号的最大/最小元素



```python
list_=[1,2,3,4,5,6,7]
print(max(list_))
print(min(list_))
```

    7
    1
    

## **注意**
**list最好不要作为变量名，否则会使list()函数失效**

# 元组（Tuple） 
使用小括号,集合起所有元素、元素值**无法更改**的列表
但是可以通过给新变量赋值来组合起原有元组
## 删除整个元组
可以通过 `del(tuple)` 来删除整个元组
##  适用方法
获取长度、添加、切分、最大最小值、for、in
## 数据集的转换
使用 `tuple(list)` 来将列表转换成元组
## 注意
tuple没有 `.reverse` 函数


```python
tup=(1,2,3,4,5)
tup2=("cat","dog")
tup3=tup+tup2
print(tup3)

list4=[1,2,3,4]
print(tuple(list4))

```

    (1, 2, 3, 4, 5, 'cat', 'dog')
    (1, 2, 3, 4)
    

## 元组访问
可以使用下标索引来访问元组中的值



```python
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
 
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])
```

    tup1[0]:  physics
    tup2[1:5]:  (2, 3, 4, 5)
    

## 单元素元组声明
元组中只包含一个元素时，需要在元素后面添加逗号


```python
tup_=(1,)
```

# 字典  
## 表示
字典的每个键值 `key:value` 对用冒号 `:` 分割，每个键值对之间用逗号 `,` 分割，整个字典包括在花括号 `{}` 中 


```python
#d = {key1 : value1, key2 : value2 }
```

## key与value引用方法  
可以通过`dict[key]`来输出对应的Value,**但是不能**通过`dict[value]`找Key  


```python
dict_={'Name':'Liu','Age':18,'Class':1}
print("dict_['Name']:",dict_['Name'])
```

    dict_['Name']: Liu
    

## 修改Key对应的Value值
通过 `dict[key]=new value`来进行新的赋值  
 **注意：键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。**


```python
dict_['Name']="ABC"
print("dict_['Name']:",dict_['Name'])
```

    dict_['Name']: ABC
    

## 删除Key对应的Value值
通过 `del dict[key]`删除对应 value  
通过 `del dict` 删除整个字典  
通过 `dict.clear()`删除整个字典的值  


```python
del dict_

dict_={'Name':'Liu','Age':18,'Class':1}
dict_.clear()
print(dict_)
```

    {}
    

## 获取字典信息  
通过`len(dict)` 获取key/value的数量  
通过`dict.items()`以元组形式列出所有的key与value值  
通过`dict.keys()` 列出所有的key值  
通过`dict.values()`列出所有的value值  


```python
dict_1={'Name':'Liu','Age':18,'Class':1}
print(len(dict_1))
print(dict_1.items())
print(dict_1.values()) 
print(dict_1.keys())
```

    3
    dict_items([('Name', 'Liu'), ('Age', 18), ('Class', 1)])
    dict_values(['Liu', 18, 1])
    dict_keys(['Name', 'Age', 'Class'])
    

## 转换字典到其他数据格式
通过 `str(dict)` 


```python
dict_={'Name':'Liu','Age':18,'Class':1}
print(str(dict_))
print(dict_.items())
```

    {'Name': 'Liu', 'Age': 18, 'Class': 1}
    dict_items([('Name', 'Liu'), ('Age', 18), ('Class', 1)])
    

# 集合（Set）  
## 性质  
1.集合中的元素**不会**重复  
2.集合中的元素**无法**更改  
3.集合**无法**使用`index.()`索引和`[]`切片(Set没有给定的顺序)  
4.可以通过循环**遍历**获得值

## 添加与移除元素

通过`set.add(value)`来添加一个元素  
通过`set.discard(value)`来删除一个元素


```python
Days= {"Mon","Tue","Wed","Wed","Thu","Fri","Sat","Sun"}
print(type(Days))
print(Days)
for Day in Days:
    print(Day)
Days.add(1)
Days.add(2)
Days.discard(2)
print(Days)

```

    <class 'set'>
    {'Sun', 'Thu', 'Fri', 'Mon', 'Wed', 'Sat', 'Tue'}
    Sun
    Thu
    Fri
    Mon
    Wed
    Sat
    Tue
    {1, 'Fri', 'Sat', 'Sun', 'Mon', 'Thu', 'Wed', 'Tue'}
    

## 集合的运算
通过`|`取两个集合的并集  
通过`&`取两个集合的交集  
通过`-`取被减集合与两个集合交集的补集  


```python
num1={1,2,3,4,5}
num2={5,6,7,8,9}
print(num1|num2)
print(num1&num2)
print(num1-num2,num2-num1)
```

    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {5}
    {1, 2, 3, 4} {8, 9, 6, 7}
    

## 判断子集
通过`<=`与`>=`来输出一个Boolean


```python
print(num1<=num2)
print((num1&num2)<=num2)
```

    False
    True
    

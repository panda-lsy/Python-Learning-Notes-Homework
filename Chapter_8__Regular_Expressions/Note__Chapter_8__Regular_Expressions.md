# 正则表达式
正则表达式通常称为模式，是一种表达式，用于指定特定目的所需的一组字符串。指定有限字符串集的简单方法是列出其元素或成员。但是通常有更简洁的方法来指定所需的字符串集。

## 正则表达式介绍
在使用正则表达式库之前，必须将其导入程序。 最简单的正则表达式库最简单的用法是 search () 函数。

## re模块
`import re`
- Python 附带的 "re "模块，主要用于字符串搜索和操作
- 还经常用于网页 "抓取"（从网站上提取大量数据）
我们将从这个简单的练习开始表达式教程，使用表达式 (w+) 和 (^)。

## rstrip()方法
Python rstrip() 删除 string 字符串末尾的指定字符，默认为空白符，包括空格、换行符、回车符、制表符。
同理,`lstrip()`删除左边,`strip()`删除的两边。

## re.search方法
re.search 扫描整个字符串并返回第一个成功的匹配。

函数语法：
`re.search(pattern, string, flags=0)`


```python
# Program
# Search for lines that contain 'is' 
import re 
hand = open('myfile.txt') 
for line in hand: 
    line = line.rstrip() 
    if re.search('is', line): 
        print(line)
```

    This is line 1
    This is line 2
    This is line 3
    This is line 4
    This is line 5
    This is line 6
    This is line 7
    This is line 8
    This is line 9
    This is line 10


当我们在搜索字符串中添加特殊字符时，正则表达式的威力就体现出来了，这些特殊字符可以让我们更精确地控制哪些行与字符串匹配。在正则表达式中添加这些特殊字符后，我们只需编写很少的代码，就能进行复杂的匹配和提取。例如，在正则表达式中，“^”用于匹配一行的 “开头”。我们可以修改程序，只匹配 “is ”位于行首的行，如下所示：


```python
# Program
# Search for lines that start with 'is' 
import re 
hand = open('myfile.txt')
for line in hand: 
    line = line.rstrip() 
    if re.search('^is', line): 
        print(line) 
```

## re.match函数
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match() 就返回 none。
函数语法：
`re.match(pattern, string, flags=0)`


```python
# Program
#!/usr/bin/python
import re
 
line = "Cats are smarter than dogs"
 
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")
```

### re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

### findall方法
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。  
注意： match 和 search 是匹配一次 findall 匹配所有。  
语法格式为：  
`findall(string[, pos[, endpos]])`  


```python
# Program
import re
text='NIIT 1234 a'
data = re.findall("[a-z]+",text)
print(data)
```

    ['a']



```python
# Program
import re
text='NIIT 1234 a'
data = re.findall("[A-Za-z]+",text)
print(data)
```

    ['NIIT', 'a']


## re.sub()方法
Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
语法：
`re.sub(pattern, repl, string, count=0, flags=0)`
参数：
- pattern : 正则中的模式字符串。
- repl : 替换的字符串，也可为一个函数。
- string : 要被查找替换的原始字符串。
- count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。


```python
# Program
import re
txt='abc edf ahs'
txt=re.sub('a','mou',txt,count=0)
print(txt)
```

    moubc edf mouhs


### re.split()方法
split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：  
`re.split(pattern, string[, maxsplit=0, flags=0])`
- pattern	匹配的正则表达式
- string	要匹配的字符串。
- maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
- flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。


```python
# Program
import re
txt='as,dq.ad,'
txt=re.split(r"\W",txt)
print(txt)
```

    ['as', 'dq', 'ad', '']


## 正则表达式（RE）语法
### 元字符
### w+ 和 ^ 表达
- "^": 该表达式匹配字符串的开头
- "w+": 该表达式匹配字符串中的字母数字字符  
下面我们将举例说明如何在代码中使用 w+ 和 ^ 表达式。


```python
# Program
import re 
xx = "Math100,education is fun" 
r1 = re.findall(r"^\w+",xx) 
print(r1) 
```

    ['Math100']


## \字符
将下一个字符标记为一个特殊字符、或一个原义字符、或一个 向后引用、或一个八进制转义符。例如，'n' 匹配字符 "n"。'\n' 匹配一个换行符。序列 '\\' 匹配 "\" 而 "\(" 则匹配 "("。

## $字符
匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置。

## \D与\d字符
\d 匹配一个数字字符。等价于 [0-9]。  
\D 匹配一个非数字字符。等价于 [^0-9]。



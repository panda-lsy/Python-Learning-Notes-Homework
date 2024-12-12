# File Handling 
## 定义文件路径
要读取或写入文本文件时，必须首先确定要写入或读取哪个文件。
## 读取和写入文件
要对文件进行写入或读取时，首先要告诉操作系统要打开文件进行读取或写入。  
读取时，将文件内容读入字符串变量。写入将字符串变量的内容写入文件。读写完成后关闭文件。  
从文件中读取文本需要三个步骤：  
1. 打开要读取的文件。  
2. 从文件中读取（通常读入字符串变量）。   
3. 关闭文件。  
以下是语法：


```python
# Program
#file object = open(file_name [, access_mode][, buffering])
```

各个参数的细节如下：

- file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
- access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
- buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。


```python
# Program
f=open('abc.txt')
f.read()
```




    'My first file\nthis file\ncontain three line\nappended data\nmore data\nwebsite\n\n \n\n\n'



### 不同模式打开文件的完全列表：

模式	描述
t	文本模式 (默认)。  
x	写模式，新建一个文件，如果该文件已存在则会报错。  
\+	打开一个文件进行更新(可读可写)。  
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。  
r+	打开一个文件用于读写。文件指针将会放在文件的开头。  
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。  
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。  
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。  
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。  

将文本写入文件需要三个类似的步骤：  
1. 打开要写入的文件。  
2. 将字符串（通常来自字符串变量）写入文件。  
3. 关闭文件。  
我们声明变量 f 来打开名为 myfile.txt 的文件。 Open 需要两个参数，一个是我们要打开的文件和一个字符串，字符串表示我们要对文件执行的权限或操作类型。
在这里，我们在参数中使用了 "w"，表示新建并写入于库中不存在的文件。加号表示读和写。


```python
# Program
f= open("myfile.txt","w+")
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
```

## 关闭文件
File 对象的 close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。  
当一个文件对象的引用被重新指定给另一个文件时，Python 会关闭之前的文件。用 close（）方法关闭文件是一个很好的习惯。  



```python
# Program
#fileObject.close()

f= open("myfile.txt","w+")
f.close()
```

## 文件定位
`tell()`方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后。  
`seek(offset [,from])`方法改变当前文件的位置。`Offset`变量表示要移动的字节数。`From`变量指定开始移动字节的参考位置。  
如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。  


```python
# Program
# Open the file in write mode and write some content to it
f= open("1.txt","w+")
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
f.write("Hello, this is a test file.")

# Move the file pointer to the beginning of the file
f.seek(0)

# Read the first 10 characters from the file
str = f.read(10)
print("读取的字符串是 : ", str)

# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)

# 把指针再次重新定位到文件开头
position = f.seek(0, 0)
str = f.read(10)
print("重新读取字符串 : ", str)

# 关闭打开的文件
f.close()
```

    读取的字符串是 :  This is li
    当前文件位置 :  10
    重新读取字符串 :  This is li


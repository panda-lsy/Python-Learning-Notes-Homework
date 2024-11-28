### 1. Write a Python program to calculate surface volume and area of a sphere. 

Note: A sphere is a perfectly round geometrical object in three-dimensional space that is the surface of a completely round ball. 



```python
import math
pi = math.pi
r = 30
print(f"The surface volume and area of a sphere is {round(4*pi*r*r,2)}")
```

    The surface volume and area of a sphere is 11309.73
    

### 2. Write a Python program to convert a string to datetime. 

Sample String: Jan 1 2019 2:43PM 

Expected Output: 2019-01-01 14:43:00 



```python
import datetime
str_time="Jan 1 2019 2:43PM"
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
mm,dd,YY,HM=str_time.split(" ")
for m in months:
    if mm == m:
        mm=months.index(m)+1
HH,MM=map(int,HM[:-2].split(":"))
if HM[-2:]=="PM":
    HH+=12
str_time_1=f"{YY}-{mm}-{dd} {HH}:{MM}:00"
fmt_time=datetime.datetime.strptime(str_time_1,"%Y-%m-%d %H:%M:%S")
print(fmt_time)
```

    2019-01-01 14:43:00
    

### 3. Write a Python program to subtract five days from current date. Go to the editor 

Sample Date 

Current Date: 2015-06-22 

5 days before Current Date: 2015-06-17



```python
import datetime
cur_time="2015-06-22"
fmt_time=datetime.datetime.strptime(cur_time,"%Y-%m-%d")
print((fmt_time-datetime.timedelta(days=5)).strftime("%Y-%m-%d"))
```

    2015-06-17
    

### 4. Write a Python script to display the various Date Time formats - Go to the editor 

a) Current date and time 

b) Current year 

c) Month of year 

d) Week number of the year 

e) Weekday of the week 

f) Day of year 

g) Day of the month 

h) Day of week 



```python
import datetime
now_time=datetime.datetime.today()
print(f"Current date and time: {now_time.strftime("%Y-%m-%d  %H:%M:%S")}")
print(f"Current year: {now_time.strftime("%Y")}")
print(f"Month of year: {now_time.strftime("%m")}")
print(f"Week number of the year: {now_time.isocalendar()[1]}")
print(f"Weekday of the week: {now_time.isocalendar()[2]}")
print(f"Day of year: {now_time.isocalendar()[1]*7+now_time.isocalendar()[2]}")
print(f"Day of the month: {now_time.strftime("%d")}")
print(f"Day of week: {now_time.strftime("%A")}")

```

    Current date and time: 2024-11-25  09:27:26
    Current year: 2024
    Month of year: 11
    Week number of the year: 48
    Weekday of the week: 1
    Day of year: 337
    Day of the month: 25
    Day of week: Monday
    

### 5. Write a Python program to generate random integers in a specific numerical range. 


```python
import random
range_=[1,100]
print(random.randint(range_[0],range_[1]))
```

    49
    

### 6. Write a Python program to list only directories, files and all directories, files in a specified path.


```python
import os,glob
path=os.getcwd()
print(f"The path is {path}")
print(f"The files in the path: {glob.glob(f"{path}/*")}")
path_=input()
os.chdir(path_)
print(f"The files in {path_}: {glob.glob(f"{path_}/*")}")
```

    The path is E:\PythonProgramming\Python-Learning-Notes-and-Homework\Python-Learning-Notes-Homework\Chapter 5 – Use of Standard Library
    The files in the path: ['E:\\PythonProgramming\\Python-Learning-Notes-and-Homework\\Python-Learning-Notes-Homework\\Chapter 5 – Use of Standard Library\\test_4_sys.py', 'E:\\PythonProgramming\\Python-Learning-Notes-and-Homework\\Python-Learning-Notes-Homework\\Chapter 5 – Use of Standard Library\\[Assignment] Chapter 5 – Use of Standard Library.ipynb', 'E:\\PythonProgramming\\Python-Learning-Notes-and-Homework\\Python-Learning-Notes-Homework\\Chapter 5 – Use of Standard Library\\[Note] Chapter 5 – Use of Standard Library.ipynb']
    The files in E:\PythonProgramming\Python-Learning-Notes-and-Homework: ['E:\\PythonProgramming\\Python-Learning-Notes-and-Homework\\Python-Learning-Notes-Homework']
    

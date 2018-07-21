# python认识数据结构 

### 1, 什么是变量

创建变量：赋值即创建

- 1.1变量命名：字母开头，不要数字，不要系统字段
- 1.2删除变量：del type

### 2，数据结构

- ##### 2.1数值本身：数字数值，字符串（‘+’，“+”，'''+'''），布尔型数值（大写开头True False）

  * st = “a,b'cdefg"

- ##### 2.2序列：list，tuple（不可变的list），字符串本身也是序列

  - list：[]包在一起
  - tuple：()
  - 索引及切片
  - 索引 list[0] list[1]
  - 切片 list[0:2] 指第1到第2个值
  - 切片是前闭后开；可以用步长 list[1:5:2]
  - 序列是可以嵌套的，里面也能嵌套字典。

### 3，映射（也叫字典） dict 键值对key value

- Dic = {'a':10,'b':"hello"}
- 无顺序
- 用key索引
- 字典也是可以嵌套的，里面也能嵌套序列。

### 4，语句

##### 4.1， 赋值语句：=

##### 4.2， 运算语句：

- 算数运算 
  - 除法2/366=0.66 
  - 乘方2**3=8  
  - 取余3%2=1 10%7=3 
  - 整除10//7=1
- 比较运算
  - a>b: True
  - a == b:  False
  - a!=b: Ture
- 逻辑运算
  - or， and， not
  - a>b or a>c: Ture

##### 4.3, 条件语句

- if, if-else, if-elif-...-else

##### 4.4 循环语句

- for, while

##### 4.5 模块语句

- import numpy as np
- import pandas as pd
- import matplolib.pyplot as plt
- rng= np.random.randn(20,2)
- data = pd.DataFrame(rng, columns = ["a","b"])
- data.plot(style = "--.k")

### 5，panda索引

- 列索引 data["姓名"]； data[[“姓名”，“年龄”]]

- 行索引 data.loc("a")

  data.iloc[2]; data.iloc[1:3]


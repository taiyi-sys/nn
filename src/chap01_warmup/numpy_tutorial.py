#!/usr/bin/env python
# coding: utf-8

# #                                           numpy 练习题

#

# ### numpy 的array操作

# #### 1.导入numpy库
import numpy as np




# #### 2.建立一个一维数组 a 初始化为[4,5,6], (1)输出a 的类型（type）(2)输出a的各维度的大小（shape）(3)输出 a的第一个元素（值为4）
a=np.array([4,5,6])
print("输出a的类型为",a.dtype)
print("输出a的各维度大小为",a.shape)
print("输出 a的第一个元素",a[0])






# #### 3.建立一个二维数组 b,初始化为 [ [4, 5, 6],[1, 2, 3]] (1)输出各维度的大小（shape）(2)输出 b(0,0)，b(0,1),b(1,1) 这三个元素（对应值分别为4,5,2）
b=np.array([[4,5,6],[1,2,3]])
print("输出a的各维度大小为",b.shape)
print("输出 b[0,0],b[0,1],b[1,1] 这三个元素为",b[0,0],b[0,1],b[1,1])




# #### 4.  (1)建立一个全0矩阵 a, 大小为 3x3; 类型为整型（提示: dtype = int）(2)建立一个全1矩阵b,大小为4x5;  (3)建立一个单位矩阵c ,大小为4x4; (4)生成一个随机数矩阵d,大小为 3x2.
a=np.zeros(shape=(3,3))
b=np.ones(shape=(4,5))
c=np.eye(4)
d=np.random.rand(3,4)



# #### 5. 建立一个数组 a,(值为[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] ) ,(1)打印a; (2)输出  下标为(2,3),(0,0) 这两个数组元素的值
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print("输出下标为(2,3),(0,0) 这两个数组元素的值为",a[2,3],a[0,0])




# #### 6.把上一题的 a数组的 0到1行 2到3列，放到b里面去，（此处不需要从新建立a,直接调用即可）(1),输出b;(2) 输出b 的（0,0）这个元素的值
b=a[0:2, 2:4]
print(b)
print("输出b 的（0,0）这个元素的值",b[0,0])




#  #### 7. 把第5题中数组a的最后两行所有元素放到 c中，（提示： a[1:2, :]）(1)输出 c ; (2) 输出 c 中第一行的最后一个元素（提示，使用 -1                 表示最后一个元素）
c=a[1:3, : ]
print(c)
print("输出 c 中第一行的最后一个元素为",c[0,-1])





# #### 8.建立数组a,初始化a为[[1, 2], [3, 4], [5, 6]]，输出 （0,0）（1,1）（2,0）这三个元素（提示： 使用 print(a[[0, 1, 2], [0, 1, 0]]) ）
a=np.array([[1,2],[3,4],[5,6]])
print("输出 （0,0）（1,1）（2,0）这三个元素为",a[[0, 1, 2], [0, 1, 0]])




# #### 9.建立矩阵a ,初始化为[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]，输出(0,0),(1,2),(2,0),(3,1) (提示使用 b = np.array([0, 2, 0, 1])                     print(a[np.arange(4), b]))
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b = np.array([0, 2, 0, 1])
print("输出(0,0),(1,2),(2,0),(3,1)为",a[np.arange(4), b])





# #### 10.对9 中输出的那四个元素，每个都加上10，然后重新输出矩阵a.(提示： b = np.array([0, 2, 0, 1]
c=a[np.arange(4), b]
c=c+10
a[np.arange(4), b]=c
print(a)







# ### array 的数学运算

# #### 11.  执行 x = np.array([1, 2])，然后输出 x 的数据类型
x = np.array([1, 2])
print("输出x的类型为",x.dtype)





# #### 12.执行 x = np.array([1.0, 2.0]) ，然后输出 x 的数据类类型
x = np.array([1.0, 2.0])
print("输出x的类型为",x.dtype)





# #### 13.执行 x = np.array([[1, 2], [3, 4]], dtype=np.float64) ，y = np.array([[5, 6], [7, 8]], dtype=np.float64)，然后输出 x+y ,和 np.add(x,y)
x = np.array([[1, 2], [3, 4]],dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
print("输出x+y为",np.add(x,y))





# #### 14. 利用 13题目中的x,y 输出 x-y 和 np.subtract(x,y)
print("输出x-y为",np.subtract(x,y))





# #### 15. 利用13题目中的x，y 输出 x*y ,和 np.multiply(x, y) 还有  np.dot(x,y),比较差异。然后自己换一个不是方阵的试试。
print("输出x*y为",x*y)
print("输出 np.multiply(x, y)为",np.multiply(x, y))
print("输出np.dot(x,y)为",np.dot(x,y))
a=np.array([1,2,3])
b=np.array([4,5,6])
print("输出a*b为",a*b)
print("输出 np.multiply(a,b)为",np.multiply(a, b))
print("输出np.dot(a,b)为",np.dot(a,b))




# #### 16. 利用13题目中的x,y,输出 x / y .(提示 ： 使用函数 np.divide())
print("输出下x/y为",np.divide(x,y))





# #### 17. 利用13题目中的x,输出 x的 开方。(提示： 使用函数 np.sqrt() )
print("输出x的开方为",np.sqrt(x))





# #### 18.利用13题目中的x,y ,执行 print(x.dot(y)) 和 print(np.dot(x,y))
print(x.dot(y))
print(np.dot(x,y))




# ##### 19.利用13题目中的 x,进行求和。提示：输出三种求和 (1)print(np.sum(x)):   (2)print(np.sum(x，axis =0 ));   (3)print(np.sum(x,axis = 1))
print("三种求和为")
print(np.sum(x))
print(np.sum(x,axis =0 ))
print(np.sum(x,axis = 1))



# #### 20.利用13题目中的 x,进行求平均数（提示：输出三种平均数(1)print(np.mean(x)) (2)print(np.mean(x,axis = 0))(3) print(np.mean(x,axis =1))）
print("输出三种平均数为")
print(np.mean(x))
print(np.mean(x,axis = 0))
print(np.mean(x,axis =1))



# #### 21.利用13题目中的x，对x 进行矩阵转置，然后输出转置后的结果，（提示： x.T 表示对 x 的转置）
print("转置数组之后数组为：")
print(x.T)





# #### 22.利用13题目中的x,求e的指数（提示： 函数 np.exp()）
print("e的指数为")
print(np.exp(x))





# #### 23.利用13题目中的 x,求值最大的下标（提示(1)print(np.argmax(x)) ,(2) print(np.argmax(x, axis =0))(3)print(np.argmax(x),axis =1))
print(np.argmax(x))
print(np.argmax(x, axis =0))
print(np.argmax(x,axis =1))





# #### 24,画图，y=x*x 其中 x = np.arange(0, 100, 0.1) （提示这里用到  matplotlib.pyplot 库）

import matplotlib.pyplot as plt
x = np.arange(0, 100, 0.1)

# 计算对应的 y 值
y = x * x

# 绘制图像
plt.plot(x, y)

# 添加标题和轴标签
plt.title('y = x * x')
plt.xlabel('x')
plt.ylabel('y')

# 显示图像
plt.show()





# #### 25.画图。画正弦函数和余弦函数， x = np.arange(0, 3 * np.pi, 0.1)(提示：这里用到 np.sin() np.cos() 函数和 matplotlib.pyplot 库)

# 生成 x 值，范围从 0 到 3π，步长为 0.1
x = np.arange(0, 3 * np.pi, 0.1)

# 计算正弦函数和余弦函数的值
y_sin = np.sin(x)
y_cos = np.cos(x)

# 绘制正弦函数图像
plt.plot(x, y_sin, label='sin(x)')

# 绘制余弦函数图像
plt.plot(x, y_cos, label='cos(x)')

# 添加标题
plt.title('Sine and Cosine Functions')

# 添加 x 轴和 y 轴标签
plt.xlabel('x')
plt.ylabel('y')

# 显示图例
plt.legend()

# 显示网格线
plt.grid(True)

# 显示图形
plt.show()





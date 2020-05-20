import math

#
#
# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
# print(enroll("yaoxilong","aa",22,"haerbin"))
#
#
# def calc(*a):
#     sum = 0
#     for n in a:
#         sum = sum + n * n
#     return sum
#
# print(calc(3,2))
#
# def enroll(name, age):
#     print('name:', name)
#     print('age:', age)
# print(enroll('姚希龙','22'))
#
#
# def quadratic(a, b, c):
#     if b * b - 4 * c * a < 0:
#         print('方程无解')
#     else:
#       x1 = (-b + math.sqrt(b * b - 4 * c * a)) / (2 * a)
#       x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
#     return x1, x2
#
# print(quadratic(1, 2, 1))
#
# print(pow(5,4))
#
#
# n1 = 100
# n2 = 1500
# L = (n1,n2)
# for x in L:
#     print("十六进制数为： "+hex(x))
#
#
# def yxl(ws):
#     if ws>0:
#         return ws
#     else: ws<0
#     return -ws
#
# print(yxl(int("1")))
#
# aa=input("您想打印的数字为：")
# # print(aa)
#
# a=100
# b=200
# l=(a,b)
# print(hex(min(l)))
# print(hex(max(l)))
#
# 计算任意n次方
# def power(x, n):
#     s = 1
#     n = abs(n)
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(2,-4))
#
# 递归函数
# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n - 1, a, c, b)#将n-1块由a绕过c搬运至b
#         print(a, '-->', c)#将最后一块最大块由a搬运至c
#         move(n - 1, b, a, c)#将b上的n-1块由把绕过a搬运至c
# move(3,"A","B","C")
#
#
# def list():
#     L = []
#     for i in range(100):
#         if i != 0 & i % 2 == 1:
#            L.append(i)
#     print(L)
#
# print(list())


# 切片
# Y = ["a","b","c","v",]
# print(Y[0:5])

# def a(str):
#     while str[-1:] == " " :
#         str = str[:-1]
#     while str[:1] == " "  :
#         str = str[1:]
#     return str
# print(a("    kobe"))

# shuzu = ["a","b","c"]
# for a,b in enumerate(shuzu):
#     print(a,b)
#
# def findone(L):
#     if L == None:
#         return (None,None)
#     else:
#         return (min(L),max(L))
#
# print(findone([1,4,3,5]))
#
# print(list(range(1, 11)))
#
# L = ['Hello', 'World', 18, 'Apple', None]
# print([s.lower() for s in L if isinstance(s,str)])


# Generator
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b  =  b, a + b
#         n = n + 1
#     return None
# print(fib(6))


# def test():
#     arr = [1]
#     while True:
#         yield arr
#         arr = [1] + [arr[i] + arr[i + 1] for i in range(len(arr) - 1)] + [1]
#         print(arr)
    

# def triangles():
#     line = [1]
#     while True:
#         try:
#            yield line
#            line = [1] + [line[i] + line[i + 1] for i in range(len(line) - 1)] + [1]
#            print(line)
#         except StopIteration as e:
#            print('Generator return value:', e.value)
#            break
# a = 'python'
# print('hello,', a or 'world')
# b = a and False
# print(b)

# import time
# from functools import reduce
#
#
# def performance(a):
#     def fn(*args, **kw):
#         t1 = time.time()
#         r = a(*args, **kw)
#         t2 = time.time()
#         print('call %s() in %fs' % (a.__name__, (t2 - t1)))
#         print(a)
#         print(fn)
#         return r
#     return fn

# @performance
# def factorial(n):
#     return reduce(lambda x,y: x*y, range(1, n+1))
# print(factorial(10))

# 装饰器
# import time
# from functools import reduce
# def yxl(f):
#     def ws(*args, **kw):
#         t1=time.time()
#         r = f(*args, **kw)
#         time.sleep(0.3)
#         t2=time.time()
#         print("执行完毕，本次执行时间为：",t2-t1)
#         print("执行完毕，本次执行结果为：",r)
#     return ws
# @yxl
# def demo(n):
#     return reduce(lambda x,y:x*y ,range(1,n))
#
# print(demo(6))

# import time
# from functools import reduce
#
#
# def performance(unit):
#     def perf_decorator(f):
#         def wrapper(*args, **kw):
#             t1 = time.time()
#             r = f(*args, **kw)
#             t2 = time.time()
#             t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
#             print('call %s() in %f %s' % (f.__name__, t, unit))
#             return r
#
#         return wrapper
#
#     return perf_decorator
#
#
# @performance('ms')
# def factorial(n):
#     return reduce(lambda x, y: x * y, range(1, n + 1))
#
#
# print(factorial(10))


# import os
#
# print(os.path.isdir(r'E:\project'))  # 判断文件夹在该地址是否存在
# print(os.path.isfile(r'E:\project'))  # 文件

# x = True
# # y = False
# # z = False
# #
# # if not x or y:
# #     print(1)
# # elif not x or not y and z:
# #     print(2)
# # elif not x or y or not y and x:
# #     print(3)
# # else:
# #     print(4)

# while 4==4:
#     print("Hello")

# i = sum = 0
# print(i,sum)
# while i<=4:
#     sum += i
#     i = i+1
#     print(i, sum)

# def Foo(x):
#     print(x)
#     if (x==1):
#         return 1
#     else:
#         return x+Foo(x-1)
#
# print(Foo(6))


# str = '最短 = 1ms，最长 = 2ms，平均 = 1ms'
# i = 0
# j = []
# res1 = list(str)
# for r in res1:
#     i += 1
#     if r == "s":
#         j.append(i)
# print(j)
# min = str[j[0]-3:j[0]-2]
# max = str[j[1]-3:j[1]-2]
# avg = str[j[2]-3:j[2]-2]
# print(min, avg, max)
# res = str[str.index("(")+1:str.index("%")+1]
# res1 = list(str)
# a = 0
# b = 0
# for r in res1:
#     b +=1
#     if r == "=":
#         a = b
# print(a)
# print(b)
# print(str[a+1:-2])

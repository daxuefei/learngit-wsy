# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#
# gen=my_generator()
# print(next(gen))
# print(next(gen))


# gen=(x*x for x in range(10))
# for num in  gen:
#     print(num)

#1.编写一个生成器函数count_up_to(n)，生成从 1 到n的整数
# def count_up_to(n):
#     for i in range(1,n+1):
#         yield i
#
# for num in count_up_to(5):
#     print(num)

#2.编写一个生成器函数 infinite_counter()，生成无限递增的整数序列。
# def infinite_counter():
#         total=0
#         while True:
#             yield total
#             total = total + 1
#
#
# gen = infinite_counter()
# for _ in range(5):
#     print(next(gen))
#3.编写一个生成器函数 fibonacci()，生成斐波那契数列。
#斐波那契数列 0，1

# def fibonacci():
#     total=0
#
#     while  total==0:
#         yield total
#         total=total+1
#     else:
#         total1=total
#         total=total1+total
#         print(total)
#         yield total
# def fibonacci():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
#
#
# gen = fibonacci()
# for _ in range(10):
#     print(next(gen))

# #编写一个生成器函数 even_numbers(n)，生成从 1 到 n 的所有偶数。
# def even_numbers(n):
#     # a=0
#     # while a<n:
#     #     a=a+2
#     #     yield a
#     return (i for i in range(2,n+2,2))
#
# for num in even_numbers(14):
#     print(num)


##使用生成器表达式生成 1 到 10 的平方数，并打印结果。
# squares = (x * x for x in range(1, 11))
# for num in squares:
#     print(num)
# for num in((x * x for x in range(1, 11))):
#     print(num)

#编写一个生成器函数 square(n)，生成 1 到 n 的平方数，然后编写另一个生成器函数 filter_odd(gen)，过滤掉奇数。将这两个生成器组合成一个管道。
# def square(n):
#     # return (i*i for i in range(1,n+1))
#     for i in range(1,n+1):
#         yield i*i
#
# def filter_odd(gen):
#     for n in gen:
#         if n%2 == 0:
#             yield n
#
# squares = square(10)
# filtered = filter_odd(squares)
# for num in filtered:
#     print(num)


###编写一个生成器函数 read_large_file(filename)，逐行读取一个大文件，并返回每一行的内容。
# def read_large_file(filename):
#     with open(filename,'r',encoding='utf-8') as file:
#         for line in file:
#             yield line.strip()
#
# for line in read_large_file("large_file.txt"):
#     print(line.strip())


###编写一个生成器函数 coroutine_example()，实现一个简单的协程，接收数据并返回处理后的结果。
def coroutine_example():
    


coroutine = coroutine_example()
next(coroutine)  # 启动协程
print(coroutine.send(10))  # 输出 20
print(coroutine.send(20))  # 输出 40
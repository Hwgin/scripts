
def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1
'''
在 Python中，使用yield返回的函数会变成一个生成器（generator）。 
在调用生成器的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行next()方法时从当前位置继续运行。
'''
gen_1 = generator(1)
gen_3 = generator(3)
print(gen_1)
print(gen_3)


def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1 = {}, next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)

get_sum(8)


# scripts
脚本练习

迭代：通过for循环遍历对象的每一个元素的过程

迭代器(Iterator)和可迭代(Iterable)的区别：
- 凡是可作用于for循环的对象都是可迭代类型；
- 凡是可作用于next()函数的对象都是迭代器类型；
- list、dict、str等是可迭代的但不是迭代器，因为next()函数无法调用它们。可以通过iter()函数将它们转换成迭代器。
- Python的for循环本质上就是通过不断调用next()函数实现的。

生成器(generator)：
- 节省内存，调用才占用内存
- 一边循环一边计算出元素的机制，称为生成器
- 可调用next()函数
- yield
- 生成器在 Python 的写法是用小括号括起来，(i for i in range(100000000))，即初始化了一个生成器。除了使用生成器推导式，我们还可以使用yield关键字

在 Python中，使用yield返回的函数会变成一个生成器（generator）。 在调用生成器的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行next()方法时从当前位置继续运行。

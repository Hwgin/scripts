# scripts
脚本练习

迭代器(Iterator)和可迭代(Iterable)的区别：
- 凡是可作用于for循环的对象都是可迭代类型；
- 凡是可作用于next()函数的对象都是迭代器类型；
- list、dict、str等是可迭代的但不是迭代器，因为next()函数无法调用它们。可以通过iter()函数将它们转换成迭代器。
- Python的for循环本质上就是通过不断调用next()函数实现的。

"""
無名関数 lambda ラムダ式
lambda 引数: 式
複雑な文は書けない
"""
def calc(x, y, c):
    return c(x, y)

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y
pwr = lambda x, y: x ** y

print(calc(6, 3, add))
print(calc(6, 3, sub))
print(calc(6, 3, mul))
print(calc(6, 3, div))
print(calc(6, 3, pwr))

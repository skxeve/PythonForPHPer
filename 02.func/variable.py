# coding=utf8

def func(*args):
    print(args)


func('hoge')
func('hoge','fuga','xyz')

def dic(**kwargs):
    print(kwargs)

dic(hoge='hoge')
dic(hoge='hoge',fuga='fuga',x='xyz')


def mixed(*args, **kwargs):
    print(args)
    print(kwargs)

mixed('hoge')
mixed('hoge', x='xyz')

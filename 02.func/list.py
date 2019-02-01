# coding=utf8

def func(hoge, piyo):
    print([hoge,piyo])

args = ['foo', 'bar']

func(*args)

kwargs = {
    'piyo': False,
    'hoge': 'test',
}
func(**kwargs)

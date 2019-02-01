# coding=utf8

class Hoge(object):
    # クラス変数
    default_value='hogehgoe'

    # メソッド内でインスタンス変数を定義する
    def __init__(self, value=None):
        if value:
            self.value = value
        else:
            self.value = self.default_value

    def get_value(self):
        return self.value

print("defualt is " + Hoge.default_value)

a = Hoge()
print(a.get_value())

b = Hoge('spappa')
print(b.get_value())

# coding=utf8

class Hoge(object):
    default_value='hogehgoe'

    def __init__(self, value=None):
        if value:
            self.value = value
        else:
            self.value = self.default_value

    def get_value(self):
        return self.value

    # 先頭に __ があるとprivateになる
    def __get_double_value(self):
        return self.value + "/" + self.value

    def get_double_value(self):
        return self.__get_double_value()

a = Hoge()
print(a.get_double_value())
print(a.__get_double_value())


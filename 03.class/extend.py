# coding=utf8

class Bird(object):
    default_speed = 10

    def __init__(self, name):
        print("Bird constructor")
        self.name = name
        self.speed = self.default_speed

    def get_info(self):
        return "name:" + self.name + ", speed:" + str(self.speed)

class Eagle(Bird):
    def __init__(self, name):
        print("Eagle constructor")
        # super(自身のクラス, 自身のインスタンス).呼びたい関数(引数)
        super(Eagle, self).__init__(name + "(Eagle)")
        self.speed = self.default_speed * 3


e = Eagle("Taro")
print(e.get_info())

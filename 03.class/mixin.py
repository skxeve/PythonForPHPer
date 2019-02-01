# coding=utf8
# Mixinは、インスタンス変数を持たずにメソッドだけを定義したクラス
# 慣例的に、クラス名にMixinを含めるようにする模様
# PHP的にはtraitに近いものだが、Mixinは言語機能ではなく手法
# Pythonで多重継承を問題点をうまく誤魔化しながら使用するために編み出された手法と考えられる


class SayMixin(object):
    def say(self):
        print("Hello Mixin!!!!!")

class Human(SayMixin, object):
    pass


human = Human()
human.say()

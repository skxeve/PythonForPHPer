# coding=utf8
# 菱形継承問題
# pythonだと多重継承が可能だが、その際
# A <- B <- D
# A <- C <- D
# となった場合に、同名メソッドや同名変数がBとCの両方に存在していた場合、期待した動作にならないこと

class Ball(object):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size

class SuperBall(Ball):
    def bound(self):
        print("bound " + str(self.get_move_length()) + "cm")
        return self

    def get_move_length(self):
        return self.size * 2

    def incr(self):
        self.size = self.size * 2
        return self

class BalanceBall(Ball):
    def roll(self):
        print("roll " + str(self.get_move_length()) + "cm")
        return self

    def get_move_length(self):
        return self.size / 2

    def incr(self):
        self.size = self.size + 1
        return self

class SuperBalanceBall(SuperBall, BalanceBall):
    pass


ball = SuperBalanceBall(40)
print("ball size is " + str(ball.get_size()))
ball.bound()
ball.roll()

# ついでにメソッドチェーンも動くか試してみたり
ball.incr().incr().bound().roll()

ball.bound().roll()

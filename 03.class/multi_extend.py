# coding=utf8

class A(object):
    def __init__(self):
        print("start A constructor")
        super(A, self).__init__()
        print("end A constructor")


class B(object):
    def __init__(self):
        print("start B constructor")
        super(B, self).__init__()
        print("end B constructor")


class C(A, B):
    def __init__(self):
        print("start C constructor")
        super(C, self).__init__()
        print("end C constructor")


i = C()

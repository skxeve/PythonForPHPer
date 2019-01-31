# coding=utf8

def greet(hour):
    """時間を指定すると、対応する挨拶を表示！"""
    if 4 < hour < 12:
        print("Good Morning")
    elif 12 <= hour < 18:
        print("Good Afternoon!")
    else:
        print("Good Evening.")

greet(4)
greet(8)
greet(12)
greet(18)

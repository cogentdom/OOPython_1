#!/usr/bin/python

class MaxSizeList(object):
    def __init__(self, max):
        self.max = max
        self.list = []

    def push(self, obj):
        self.list.append(obj)
        if len(self.list) > self.max:
            self.list.pop(0)

    def get_list(self):
        return self.list


a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())






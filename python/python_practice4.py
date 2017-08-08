'''
def author()
    Jonathan James
import random
random.randint(1,200)

class MyClass:
    def __init__(self, my_name):
        self.name = my_name

    def getName(self):
        return 'Hello ' + self.name

M1 = MyClass("Brooklyn")
M2 = MyClass("Atlanta")

print M1.getName()
print M2.getName()


def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'


for x in [-1, 0, 1]:
    print(sign(x))


class Greeter:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(self.name)


g = Greeter("param")

g.greet()

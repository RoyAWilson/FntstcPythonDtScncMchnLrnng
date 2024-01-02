name = 'Linda'
age = 27


def greeting():
    print('Linda is saying hello')


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f'{self.name} is taking a walk outside')

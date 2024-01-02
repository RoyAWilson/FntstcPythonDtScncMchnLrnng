''''
Lecture  114 Basics of Python Modules
'''

import module_1 as mod1

a: int = 100
b: int = 2
name: str = 'Roy'
print(a*b)
print(name)
print(mod1.name)
print(mod1.age)

mod1.greeting()
tom = mod1.Person('Tom', 33)
tom.walk()

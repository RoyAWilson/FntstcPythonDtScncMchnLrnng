''''
Lecture  114 Basics of Python Modules
'''

import module_1 as mod1

from Robot import cleaning, cooking, washing
from Robot.childcare.playingwithchildren import play
from Robot.childcare import childsitting, playingwithchildren
from Robot.childcare import childsitting

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

cleaning.clean('Master Bedroom')
print(cooking.dishes)
cooking.cook(cooking.dishes[1])
washing.wash()

play()

print(childsitting.child)
cleaning
childsitting
play

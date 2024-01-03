# # Absolute import
# import Robot.cooking

# Relative import

from ..cooking import cook
from .playingwithchildren import play

child = 'Lucy'
cook(dish='Pasta and Milk')
play()

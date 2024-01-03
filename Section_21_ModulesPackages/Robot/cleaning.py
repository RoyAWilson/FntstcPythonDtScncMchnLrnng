# Importing a sibling package Lecture 117 - Absolute import

from Robot.cooking import dishes, cook
from Robot.childcare.playingwithchildren import play


def clean(room: str):

    print(f'The robot is cleaning room {room}')
    # print('The cleaning robot is also cooking a dish')
    # cook(dishes[-1])
    # print(play())

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)
print(Color.YELLOW)
for color in Color:
    print(color)

# auto assigning value
from enum import Enum, auto
class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
print(Color.RED.value)
print(Color.GREEN.value)
print(Color.BLUE.value)

# using enum in conditional statements
def describe_color(color):
    if color == Color.RED:
        return"The color is red"
    elif color == Color.GREEN:
        return"The color is green"
    elif color == Color.BLUE:
        return"The color is blue"
print(describe_color(Color.RED))

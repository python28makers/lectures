""" Ассоциация """
# Ассоциация - принцип ООП, который описывает виды связей между классами

# Ассоциация - делится на композицию и агрегацию.


class Window:
    def __init__(self, height, width):
        self.height = height
        self.width = width

class Brick:
    def __init__(self, color, durability):
        self.color = color
        self.durability = durability


class House:
    def __init__(
            self, 
            height: int, 
            width: int, 
            area: int, 
            window: Window, 
            brick: Brick):
        self.height = height
        self.width = width
        self.area = area
        self.window = window
        self.brick = brick


window = Window(150, 150)
brick = Brick('orange', 'high')
house = House(1000, 1000, 10*10, window, brick)
house.brick.color # 'orange'
# Агрегация - слабая связь между классами - объекты разных классов создаются независимо друг от друга


class CompositeHouse:
    def __init__(self, heigth, width, area, w_heigth, w_width, b_color, b_durability):
        self.heigth = heigth
        self.width = width
        self.area = area
        self.window = Window(w_heigth, w_width)
        self.brick = Brick(b_color, b_durability)


composite_house = CompositeHouse(1000, 1000, 10*10, 150, 150, 'red', 'middle')
composite_house
# Композиция - сильная связь между классами - объекты связанных классов не могут создаваться по отдельности
        

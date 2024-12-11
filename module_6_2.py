class Vehicle:
    __COLOR_VARIANTS = ['red', 'green', 'black', 'purple', 'blue']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power} лошадиных сил'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{Vehicle.get_model(self)} \n{Vehicle.get_horsepower(self)} \n{Vehicle.get_color(self)} \nВладелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in Vehicle.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', '500', 'purple')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
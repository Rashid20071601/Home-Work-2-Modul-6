# Определяем базовый класс Vehicle (Транспортное средство)
class Vehicle:
    # Закрытый список вариантов цветов
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    # Конструктор класса, инициализирует объект с владельцем, моделью, цветом и мощностью двигателя
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # Сохраняем имя владельца
        self.__model = model  # Закрытое свойство для модели автомобиля
        self.__color = color  # Закрытое свойство для цвета автомобиля
        self.__engine_power = int(engine_power)  # Закрытое свойство для мощности двигателя, преобразуем в целое число

    # Метод для получения информации о модели
    def get_model(self):
        return f"Модель: {self.__model}"

    # Метод для получения информации о мощности двигателя
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    # Метод для получения информации о цвете
    def get_color(self):
        return f"Цвет: {self.__color}"

    # Метод для печати всей информации о транспортном средстве
    def print_info(self):
        print(f"{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}")

    # Метод для изменения цвета автомобиля
    def set_color(self, new_color):
        # Приводим все цвета к нижнему регистру для сравнения
        # Проверяем, есть ли новый цвет в списке доступных цветов
        if new_color.lower() in list(map(str.lower, self.__COLOR_VARIANTS)):
            self.__color = new_color  # Изменяем цвет
        else:
            print(f"Нельзя сменить цвет на {new_color}")  # Сообщаем об ошибке, если цвет недоступен


# Определяем класс Sedan, который наследует от Vehicle
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Закрытое свойство для ограничения количества пассажиров


# Создаем экземпляр класса Sedan с заданными параметрами
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Печатаем изначальные свойства автомобиля
vehicle1.print_info()

# Меняем цвет на недопустимый цвет 'Pink' и проверяем
vehicle1.set_color('Pink')  # Это должно вывести сообщение об ошибке
# Меняем цвет на допустимый цвет 'BLACK'
vehicle1.set_color('BLACK')
# Меняем владельца
vehicle1.owner = 'Vasyok'

# Печатаем обновленную информацию о автомобиле
vehicle1.print_info()

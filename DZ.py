# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата
class NumberConverter:
    def __init__(self, input_number):
        self.number = input_number

    def get_number(self):
        change = format(self.number, '#x')
        return f'{change} - оно'


if __name__ == '__main__':
    number = NumberConverter(125)
    print(number.get_number())

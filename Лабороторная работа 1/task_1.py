import doctest

class Building:
    def __init__(self, name: str, height: float):
        """
        Инициализация объекта "Здание".

        :param name: Название здания
        :param height: Высота здания
        """
        self.name = name
        self.height = height

    def change_color(self, color: str) -> None:
        """
        Изменение цвета здания.

        :param color: Цвет, на который нужно изменить здание
        """
        ...

    def add_floor(self, number_of_floors: int) -> None:
        """
        Добавление этажей к зданию.

        :param number_of_floors: Количество этажей, которое нужно добавить
        """
        ...

    def renovate(self, budget: float) -> None:
        """
        Реставрация здания по указанному бюджету.

        :param budget: Бюджет на реставрацию
        """
        ...


class Product:
    def __init__(self, name: str, price: float):
        """
        Инициализация объекта "Продукт".

        :param name: Название продукта
        :param price: Цена продукта
        """
        self.name = name
        self.price = price

    def apply_discount(self, discount: float) -> None:
        """
        Применение скидки к продукту.

        :param discount: Размер скидки в процентах
        """
        ...

    def check_availability(self, quantity: int) -> bool:
        """
        Проверка наличия продукта в указанном количестве.

        :param quantity: Количество продукта для проверки
        :return: Наличие продукта в указанном количестве
        """
        ...


class MobileDevice:
    def __init__(self, brand: str, model: str):
        """
        Инициализация объекта "Мобильное устройство".

        :param brand: Марка мобильного устройства
        :param model: Модель мобильного устройства
        """
        self.brand = brand
        self.model = model

    def make_call(self, number: str) -> None:
        """
        Осуществление звонка на указанный номер.

        :param number: Номер, на который нужно позвонить
        """
        ...

    def send_message(self, contact: str, message: str) -> None:
        """
        Отправка сообщения указанному контакту.

        :param contact: Контакт, которому нужно отправить сообщение
        :param message: Текст сообщения
        """
        ...

    def take_photo(self) -> None:
        """
        Съемка фотографии.
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
import doctest

class Glass:
    """
        Документация на класс.
        Класс описывает модель стакана.
    """

    def __init__(self, height: float, bottom_radius: float):
        """
         Создание и подготовка к работе объекта Стакан.
         :param height: высота стакана
         :param bottom_radius: радиус дня стакана
         Примеры:
         >>> glass = Glass(50.0, 10.0)  # инициализация экземпляра класса
         """

        if not isinstance(height, float):
            raise TypeError("Высота стакана должна быть типа float")
        if height <= 0:
            raise ValueError("Высота стакана должна быть положительным числом")
        self.height = height

        if not isinstance(bottom_radius, float):
            raise TypeError("Радиус дна должен быть float")
        if bottom_radius <= 0:
            raise ValueError("Радиус дна должен быть положительным числом")
        self.bottom_radius = bottom_radius

    def count_volume(self):
        """
                Функция которая позволяет вычислить объем стакана
                :return: Объем стакана
                Примеры:
                >>> glass = Glass(30.0, 10.0)
                >>> glass.count_volume()
        """
        ...

    def count_another_height(self, new_bottom_radius: float) ->float:
        """
            Функция, которая позволяет вычислить новую высоту стакана для заданного радиуса, и такого же объема,
            как имеющийся стакан
            :return: Объем стакана
            Примеры:
            >>> glass = Glass(30.0, 10.0)
            >>> glass.count_another_height(15.0)
        """
        if new_bottom_radius <= 0:
            raise ValueError("Радиус стакана должна быть положительным числом")
        ...

class Tumba:
    """
        Документация на класс.
        Класс описывает модель тумбы.
    """

    def __init__(self, edge: float, things: float):
        """
         Создание и подготовка к работе объекта Тумба.
         :param edge: ребро тумбы
         :param things: количество вещей внутри
         Примеры:
         >>> tumba = Tumba(50.0,10.0)  # инициализация экземпляра класса
         """

        if not isinstance(edge, float):
            raise TypeError("Ребро тумбы должно быть типа float")
        if edge <= 0:
            raise ValueError("Ребро тумбы должно быть быть положительным числом")
        self.edge = edge

        if not isinstance(things, float):
            raise TypeError("Объем вещей внутри должно быть типа float")
        if things <= 0:
            raise ValueError("Объем вещей внутри быть быть положительным числом")
        self.things = things

    def count_volume(self) -> float:
        """
                Функция которая позволяет вычислить объем тумбы
                :return: Объем тумбы
                Примеры:
                >>> tumba = Tumba(30.0, 10.0)
                >>> tumba.count_volume()
        """
        ...

    def is_empty_cube(self) -> bool:
        """
        Функция, которая проверяет является ли тумба пустой
        :return: Является ли тумба пустой
        Примеры:
        >>> tumba = Tumba(30.0, 10.0)
        >>> tumba.is_empty_tumba()
        """
        ...

class Apartment:
    """
        Документация на класс.
        Класс описывает модель квартиры.
    """

    def __init__(self, room: int, occupied_rooms: int):
        """
         Создание и подготовка к работе объекта квартира.
         :param room: количество комнат в квартире
         :param occupied_rooms: количество занятых комнат в квартире
         Примеры:
         >>> apartment = Apartment(10,10)  # инициализация экземпляра класса
         """

        if not isinstance(room, int):
            raise TypeError("Количество комнат в квартире должно быть типа int")
        if room <= 0:
            raise ValueError("Количество комнат в квартире должно быть быть положительным числом")
        self.room = room

        if not isinstance(occupied_rooms, int):
            raise TypeError("количество занятых комнат в квартире  должно быть типа int")
        if occupied_rooms <= 0:
            raise ValueError("количество занятых комнат в квартире должно быть быть положительным числом")
        self.occupied_rooms = occupied_rooms

    def count_volume(self) -> int:
        """
                Функция которая позволяет вычислить количество комнат в квартире
                :return: Количество комнат в квартире
                Примеры:
                >>> apartment = Apartment(10,10)
                >>> apartment.count_volume()
        """
        ...

    def is_empty_house(self) -> bool:
        """
        Функция которая проверяет есть ли в доме свободный квартиры
        :return: Является ли дом полностью пустым
        Примеры:
        >>> apartment = Apartment(10,10)
        >>> apartment.is_empty_apartament()
        """
        ...



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()
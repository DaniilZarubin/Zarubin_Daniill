if __name__ == "__main__":
    class BaseAnimal:

        def __init__(self, name: str):
            self.name = name

        def __str__(self) -> str:
            return f"{self.__class__.__name__}: {self.name}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r})"


    class SubMammal(BaseAnimal):
        """
        Дочерний класс млекопитающее для класса животное расширяет функционал базового класса.
        """

        def __init__(self, name: str, habitat: str):
            super().__init__(name)
            self.habitat = habitat

        def sound(self) -> str:
            """
            Возвращает звук, издаваемый данным млекопитающим.
            """
            if self.name.lower() == "lion":
                return "Roar"
            elif self.name.lower() == "elephant":
                return "Trumpet"
            else:
                return "Unknown sound"

    pass

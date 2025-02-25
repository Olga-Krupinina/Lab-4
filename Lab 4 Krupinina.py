class Transport:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self._brand = brand
        self._model = model
        self._year = year

    def __str__(self) -> str:
        return f"{self._brand} {self._model} ({self._year})"

    def __repr__(self) -> str:
        return f"Transport(brand='{self._brand}', model='{self._model}', year={self._year})"

    def start_engine(self) -> str:
        return f"{self._brand} {self._model} engine started."


class Car(Transport):
    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        super().__init__(brand, model, year)
        self._doors = doors

    def __str__(self) -> str:
        return f"{super().__str__()} with {self._doors} doors"

    def start_engine(self) -> str:
        return f"{super().start_engine()} This car has {self._doors} doors."


class Truck(Transport):
    def __init__(self, brand: str, model: str, year: int, capacity: float) -> None:
        super().__init__(brand, model, year)
        self._capacity = capacity

    def __str__(self) -> str:
        return f"{super().__str__()} with a capacity of {self._capacity} tons"

    def start_engine(self) -> str:
        return f"{super().start_engine()} This truck has a capacity of {self._capacity} tons."

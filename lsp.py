"""
L — Liskov Substitution Principle (Принцип підстановки Лісков).

Об'єкти підкласу повинні замінювати об'єкти базового класу
без порушення коректності програми.

Погано: Penguin успадковує Bird.fly(), але кидає виняток — підстановка ламає код.
Добре: здатність літати винесена в окрему абстракцію.
"""
from abc import ABC, abstractmethod


# ---------- Порушення принципу ----------
class BadBird:
    def fly(self) -> str:
        return "Летить"


class BadPenguin(BadBird):
    def fly(self) -> str:
        raise NotImplementedError("Пінгвіни не літають")  # ламає очікування клієнта


# ---------- Дотримання принципу ----------
class Bird(ABC):
    @abstractmethod
    def move(self) -> str: ...


class FlyingBird(Bird):
    def move(self) -> str:
        return self.fly()

    def fly(self) -> str:
        return f"{type(self).__name__} летить"


class Sparrow(FlyingBird):
    pass


class Penguin(Bird):
    def move(self) -> str:
        return "Penguin пливе"


def make_birds_move(birds: list[Bird]) -> None:
    # працює з будь-яким підкласом Bird без перевірок типу
    for bird in birds:
        print(bird.move())


if __name__ == "__main__":
    make_birds_move([Sparrow(), Penguin()])

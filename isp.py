"""
I — Interface Segregation Principle (Принцип розділення інтерфейсу).

Клієнти не повинні залежати від методів, якими вони не користуються.
Краще кілька вузьких інтерфейсів, ніж один «товстий».

Погано: простий принтер змушений реалізовувати scan() і fax().
Добре: окремі інтерфейси Printer, Scanner, Fax.
"""
from abc import ABC, abstractmethod


# ---------- Порушення принципу ----------
class BadMachine(ABC):
    @abstractmethod
    def print(self, doc: str) -> None: ...
    @abstractmethod
    def scan(self, doc: str) -> None: ...
    @abstractmethod
    def fax(self, doc: str) -> None: ...


class BadSimplePrinter(BadMachine):
    def print(self, doc: str) -> None:
        print("Друк:", doc)

    def scan(self, doc: str) -> None:
        raise NotImplementedError  # змушені реалізовувати непотрібне

    def fax(self, doc: str) -> None:
        raise NotImplementedError


# ---------- Дотримання принципу ----------
class Printer(ABC):
    @abstractmethod
    def print(self, doc: str) -> None: ...


class Scanner(ABC):
    @abstractmethod
    def scan(self, doc: str) -> None: ...


class Fax(ABC):
    @abstractmethod
    def fax(self, doc: str) -> None: ...


class SimplePrinter(Printer):
    def print(self, doc: str) -> None:
        print("Друк:", doc)


class MultiFunctionDevice(Printer, Scanner, Fax):
    def print(self, doc: str) -> None:
        print("МФП друк:", doc)

    def scan(self, doc: str) -> None:
        print("МФП сканування:", doc)

    def fax(self, doc: str) -> None:
        print("МФП факс:", doc)


if __name__ == "__main__":
    SimplePrinter().print("Звіт.pdf")
    mfd = MultiFunctionDevice()
    mfd.scan("Договір.pdf")
    mfd.fax("Договір.pdf")

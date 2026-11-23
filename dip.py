"""
D — Dependency Inversion Principle (Принцип інверсії залежностей).

Модулі верхнього рівня не повинні залежати від модулів нижнього рівня —
обидва мають залежати від абстракцій. Абстракції не залежать від деталей.

Погано: OrderService сам створює MySQLDatabase і жорстко до неї прив'язаний.
Добре: OrderService залежить від абстракції Database, конкретна БД передається ззовні.
"""
from abc import ABC, abstractmethod


# ---------- Порушення принципу ----------
class MySQLDatabase:
    def save(self, data: str) -> None:
        print("MySQL: збережено", data)


class BadOrderService:
    def __init__(self):
        self.db = MySQLDatabase()  # жорстка залежність від конкретної реалізації

    def create_order(self, item: str) -> None:
        self.db.save(item)


# ---------- Дотримання принципу ----------
class Database(ABC):
    @abstractmethod
    def save(self, data: str) -> None: ...


class PostgresDatabase(Database):
    def save(self, data: str) -> None:
        print("PostgreSQL: збережено", data)


class InMemoryDatabase(Database):
    def __init__(self):
        self.items: list[str] = []

    def save(self, data: str) -> None:
        self.items.append(data)
        print("InMemory: збережено", data)


class OrderService:
    def __init__(self, db: Database):  # залежність впроваджується ззовні
        self.db = db

    def create_order(self, item: str) -> None:
        self.db.save(item)


if __name__ == "__main__":
    OrderService(PostgresDatabase()).create_order("Ноутбук")
    OrderService(InMemoryDatabase()).create_order("Мишка")  # зручно для тестів

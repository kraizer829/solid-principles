"""
O — Open/Closed Principle (Принцип відкритості/закритості).

Програмні сутності мають бути відкриті для розширення, але закриті для змін.

Погано: щоб додати нову знижку, треба редагувати if/elif у функції.
Добре: нова знижка — це новий клас, існуючий код не змінюється.
"""
from abc import ABC, abstractmethod


# ---------- Порушення принципу ----------
def bad_discount(customer_type: str, price: float) -> float:
    if customer_type == "regular":
        return price
    elif customer_type == "vip":
        return price * 0.8
    # новий тип клієнта => доведеться змінювати цю функцію
    return price


# ---------- Дотримання принципу ----------
class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float: ...


class NoDiscount(Discount):
    def apply(self, price: float) -> float:
        return price


class VipDiscount(Discount):
    def apply(self, price: float) -> float:
        return price * 0.8


class StudentDiscount(Discount):  # розширення без зміни існуючого коду
    def apply(self, price: float) -> float:
        return price * 0.9


class PriceCalculator:
    def __init__(self, discount: Discount):
        self.discount = discount

    def final_price(self, price: float) -> float:
        return round(self.discount.apply(price), 2)


if __name__ == "__main__":
    for d in (NoDiscount(), VipDiscount(), StudentDiscount()):
        print(type(d).__name__, PriceCalculator(d).final_price(1000))

"""
S — Single Responsibility Principle (Принцип єдиної відповідальності).

Клас повинен мати лише одну причину для зміни.

Погано: клас Report і формує дані, і форматує їх, і зберігає у файл.
Добре: кожна відповідальність винесена в окремий клас.
"""


# ---------- Порушення принципу ----------
class BadReport:
    def __init__(self, title: str, rows: list[str]):
        self.title = title
        self.rows = rows

    def to_text(self) -> str:                 # відповідальність 1: форматування
        return self.title + "\n" + "\n".join(self.rows)

    def save(self, path: str) -> None:        # відповідальність 2: збереження
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.to_text())


# ---------- Дотримання принципу ----------
class Report:
    """Лише зберігає дані звіту."""

    def __init__(self, title: str, rows: list[str]):
        self.title = title
        self.rows = rows


class ReportFormatter:
    """Лише форматує звіт у текст."""

    def format(self, report: Report) -> str:
        return report.title + "\n" + "\n".join(f"- {r}" for r in report.rows)


class ReportSaver:
    """Лише зберігає готовий текст у файл."""

    def save(self, text: str, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    report = Report("Продажі за листопад", ["Товар A: 10", "Товар B: 25"])
    text = ReportFormatter().format(report)
    print(text)
    ReportSaver().save(text, "report.txt")

"""Demonstrates different auto() value generation behaviors in Python's Enum."""

from enum import Enum, auto


class DefaultDay(Enum):
    """Enum using default auto() value generation (1, 2, 3, ...)."""

    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


class CustomEnum(Enum):
    """Enum subclass that generates 3-letter lowercase values."""

    @staticmethod
    def _generate_next_value_(name, _start, _count, _last_values):
        """Generate custom values as lowercase 3-letter abbreviations."""
        return name.lower()[:3]


class CustomDay(CustomEnum):
    """Day enum using custom 3-letter value generation."""

    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


def main():
    """Display both default and custom auto() behaviors."""
    print("Default auto() behavior:")
    for day in DefaultDay:
        print(f"{day.name}: {day.value}")

    print("\nCustom auto() behavior:")
    for day in CustomDay:
        print(f"{day.name}: {day.value}")


if __name__ == "__main__":
    main()


class Supperhero:
    def __init__(self, name: str, strength_level: int):
        self.name = name
        self.strength_level = strength_level

    def __str__(self) -> str:
        return self.name

    def is_stronger_than(self, other: "Supperhero") -> bool:
        return self.strength_level > other.strength_level

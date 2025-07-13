## 🧱 Step 1: Supperhero Class (`app.py`)

```python
class Supperhero:
    def __init__(self, name: str, strength_level: int):
        self.name = name
        self.strength_level = strength_level

    def __str__(self) -> str:
        return self.name

    def is_stronger_than(self, other: "Supperhero") -> bool:
        return self.strength_level > other.strength_level
        ```

- __init__: Sets up the name and strength of a hero.

- __str__: Returns the name when printed.

- is_stronger_than(): Compares strength between two heroes.

## Create Unit Test File (test_app.py)
```
import unittest
from app import Supperhero

class TestSupperhero(unittest.TestCase):

    def setUp(self):
        # This runs before each test
        self.hero1 = Supperhero("Hero1", 10)
        self.hero2 = Supperhero("Hero2", 5)
        self.hero3 = Supperhero("Hero3", 10)

    def test_stronger_hero(self):
        self.assertTrue(self.hero1.is_stronger_than(self.hero2))

    def test_weaker_hero(self):
        self.assertFalse(self.hero2.is_stronger_than(self.hero1))

    def test_equal_strength(self):
        self.assertFalse(self.hero1.is_stronger_than(self.hero3))
        self.assertFalse(self.hero3.is_stronger_than(self.hero1))

    def test_str_method(self):
        self.assertEqual(str(self.hero1), "Hero1")

if __name__ == "__main__":
    unittest.main()
```

| Code/Part              | Explanation                                       |
|------------------------|---------------------------------------------------|
| `import unittest`      | Loads Python's built-in testing tools             |
| `from app import Supperhero` | Imports the class to test                    |
| `setUp()`              | Runs before each test — creates reusable test data|
| `assertTrue(condition)`| Test passes if the condition is `True`            |
| `assertFalse(condition)`| Test passes if the condition is `False`          |
| `assertEqual(a, b)`    | Test passes if `a` equals `b`                     |
| `unittest.main()`      | Runs all test methods when the file is executed   |

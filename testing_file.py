class Dog:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year


dog = Dog("Bubbles", 2022)

print(f"{dog.name:s} was born in {dog.birth_year:d}")

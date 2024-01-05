# As per previous examples please create an example of your own.
# The abstract class should contain five (3 abstract and 2 normal ) methods.
# Create 2 subclasses that would inherit abstract class.

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self) -> str:
        pass

    @abstractmethod
    def get_vaccines(self) -> str:
        pass

    @abstractmethod
    def get_paws_count(self) -> int:
        pass

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age


class Dog(Animal):
    def speak(self) -> str:
        return "Dog says Woof!"

    def get_vaccines(self) -> str:
        return "Adenovirus vaccine"

    def get_paws_count(self) -> int:
        return 4


class Cat(Animal):
    def speak(self) -> str:
        return "Cat says Meow!"


dog = Dog(name="Lassie", age=6)

# cat = Cat(name="Garfield", age=2)

print(dog.get_name())
print(dog.speak())
print(dog.get_vaccines())
print(dog.get_paws_count())

# Create an abstract class Animal with which takes name of animal as an input and initialize it.
# The create speak abstract method, to be overridden by subclasses. And get_name method which returns name of the animal.
# Now create two subclasses of Animals: Dog and Cat which overrides the speak method,
# and provide the implementation which returns a string "Dog says Woof!" and "Cat says Meow!" respectively.
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    @abstractmethod
    def speak(self) -> str:
        pass


class Dog(Animal):
    def speak(self) -> str:
        return "Dog says Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return "Cat says Meow!"


name = input("Enter animal name: ")

dog = Dog(name=name)

print(dog.get_name())
print(dog.speak())

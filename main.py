from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_vehicle_type(self) -> str:
        pass

    def get_color(self) -> str:
        return "Black"


class Plane(Vehicle):
    def get_vehicle_type(self) -> str:
        return "Plane"


plane = Plane()

print(plane.get_color())

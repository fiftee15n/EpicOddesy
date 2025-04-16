from abc import ABC, abstractmethod

# we used abstract class and method to keep a track  to our task : Abstraction
class Task(ABC):
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def update_action(self):
        pass
    @abstractmethod
    def draw(self):
        pass
    def load_images(self):
        pass
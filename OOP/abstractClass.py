#python does not provide the abstract class itself . we have to use the abc module of python.

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def bread(self):
        print("this is Animal bread")

    #concrete method.
    def haslegs(self):
        print("yes I have legs")


class Dog(Animal):
    def bread(self):
        super().bread()
        print("I am dog")


if __name__ == '__main__':
    # animal = Animal()             #can't be instantiated as it is a abstract class

    dog = Dog()
    dog.bread()
    dog.haslegs()

  


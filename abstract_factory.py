#!/usr/bin/env python
# coding: utf-8

"""
    @author: Jgirl
    @time: 16-2-15 下午8:02
    @function:抽象工厂模式
"""
import random


# 抽象工厂类
class PetShop:  # 宠物类
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print("This is a lovely", pet)
        print("It says", pet.speak())
        print("It eats", self.pet_factory.get_food())


class Dog:
    def __init__(self):
        pass

    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat:
    def __init__(self):
        pass

    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# 具体工厂类
class DogFactory:  # 狗厂类
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory:  # 猫厂类
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


def get_factory():
    return random.choice([DogFactory, CatFactory])()


if __name__ == "__main__":
    shop = PetShop()
    print shop
    for i in range(3):
        shop.pet_factory = get_factory()  # 指定是什么工厂，具体生产什么类型的产品
        shop.show_pet()
        print("=" * 20)

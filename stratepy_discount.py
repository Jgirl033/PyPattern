#!/usr/bin/env python
# coding: utf-8

"""
    @author: Jgirl
    @time: 16-2-16 下午2:50
    @function:策略模式－商场打折案例
"""
import types


class DiscountStrategy:  # 根据不同的需求对打折方案进行选择
    def __init__(self, func=None):
        self.discount_strategy = '打七五折'
        if func is not None:
            self.execute = types.MethodType(func, self)  # 将实例与具体的方案进行绑定

    def execute(self):
        print(self.discount_strategy)


def execute_strategy1(self):
    print(self.discount_strategy)


def execute_strategy2(self):
    print(self.discount_strategy)


if __name__ == '__main__':
    discount0 = DiscountStrategy()
    discount0.execute()

    discount1 = DiscountStrategy(execute_strategy1)
    discount1.discount_strategy = '打九折'
    discount1.execute()

    discount2 = DiscountStrategy(execute_strategy2)
    discount2.discount_strategy = '打八折'
    discount2.execute()

#!/usr/bin/env python
# coding: utf-8

"""
    @author: Jgirl
    @time: 16-2-17 下午10:39
    @function:原型模式
"""
import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):  # 创建对象
        self._objects[name] = obj

    def unregister_object(self, name):  # 删除对象
        del self._objects[name]

    def clone(self, name, **attr):  # 复制对象并更新属性，动态绑定
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


def main():
    class A:
        def __init__(self):
            pass

    a = A()
    prototype = Prototype()
    prototype.register_object('a', a)
    b = prototype.clone('a', a=1, b=2, c=3)

    print(a)
    print(b.a, b.b, b.c)


if __name__ == '__main__':
    main()

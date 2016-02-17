#!/usr/bin/env python
# coding: utf-8

"""
    @author: Jgirl
    @time: 16-2-15 下午8:32
    @function:工厂模式
"""


class GreekGetter:
    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)


class EnglishGetter:
    def __init__(self):
        pass

    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):  # 确定选取某个工厂生产,language相当于工厂参数
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()


e, g = get_localizer("English"), get_localizer("Greek")
for msgid in "dog parrot cat bear".split():
    print(e.get(msgid))
    print(g.get(msgid))

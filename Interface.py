# interface在python是沒有keyword可以使用的，
# 因此使用@staticmethod

import random
from abc import ABCMeta, abstractmethod


class Flyer(metaclass=ABCMeta):  # 就像是Java中的interface
    @abstractmethod
    def fly(self):
        pass

class Bird:
    pass

class Sparrow(Bird, Flyer):  # 就像Java中繼承Bird類別並實作Flyer介面
    def fly(self):
        print('麻雀飛')

s = Sparrow()
s.fly()  # 麻雀飛
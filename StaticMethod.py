#static methods用法就像是說在這個東西創建時，需要給一個前提，檢查是否這個物件能被創建
#static method顧名思義就是可以不用創建物件就直接呼叫，跟Java使用方式一樣

from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以用以下這種方式來做到方法的調用，只是參數要是object本身
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('無法成為三角形.')


if __name__ == '__main__':
    main()

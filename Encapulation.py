#封裝是指隱藏object中一些不希望被外部所訪問到的屬性、方法
#如何隱藏一個object的屬性？
#   - 將object的屬性名，修改為一個外部不知道的名字
#如何獲取(修改)object中的屬性？
#   - 需要利用getter和setter方法使外部可以訪問到屬性
#   - getter：獲取對象中的指定屬性(get_屬性)
#   - setter：用來設定對象的指定屬性(set_屬性)
#   - getter 和 setter可以用decorator來表示: @name.setter
class Dog:
    def __init__(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

d = Dog('Max')
d.set_name('Lol')
print(d.get_name()) #Lol

class Cat:
    def __init__(self, name):
        self.__name = name
        
    #property裝飾器，用來將一個get方法，轉換成為object屬性
    #添加property裝飾器以後，我們就可以像是調用屬性一樣使用get方法
    #使用property裝飾器的方法，必須和屬性名稱必須要一樣
    @property 
    def name(self):
        print('getter執行，不是屬性執行')
        return self.__name
    #setter方法的裝飾器
    @name.setter
    def name(self, name):
        print('setter method執行，不是屬性執行')
        self.__name = name

d = Cat('Meow')
d.name = 'NOOO' #setter method執行，不是屬性執行
print(d.name) #getter執行，不是屬性執行 \n NOOO  ->這時候是調用name這個method，就不是調用屬性

#可以利用把object屬性使用雙底線__xxx
#__xxx是object的隱藏數ㄓㄧㄥ，只能在class的內部訪問，無法通過object訪問(但其實實際上還是可以)
print(d._Cat__name) #利用這樣的方式還是可以訪問到

#但是這樣__其實一般是不用的，
#都會把隱藏屬性都以_開頭
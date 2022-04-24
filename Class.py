# 目前所學的object都是built-in object
# 在開發當中一定會要自訂object
# 像是int(), float(), bool()...都是class

# class class_name (super class):

class MyClass:
    pass

mc = MyClass()
result = isinstance(mc, MyClass) #isinstance(): 用來檢查一個object是否為某class的instance
print(result) # True

#class也是一個object
#class其實也就是用來創建object的object
#class是一個type類型的object，定義class實際上就是定義了一個type類型的對象
#因此class也會被賦予一個id, type, value (type=<lass 'type'>)
#然後會將MyClass的reference指向到memory中的id去

#創建class的流程：
# 1. 一樣會在memory當中創建一個空間，並且創建一個variable mc
# 2. 在memory中會有一個新的object出現
# 3. 將object的id賦予給variable 'mc', 並且type會是'MyClass'
# => variable會被reference到memory當中的id位置


#object中的variable稱為field
#使用object.field = field_value
class MyClass():
    name = 10
mc = MyClass()
print(mc.name) # 10

#object都由兩個部分構成：
# 1. 數據(屬性)
# 2. 行為(方法)

class Person:
    #在ckass中定義的variable, 都會成為所有instance的public屬性
    #也就是說所有instance都可以訪問這些variable
    name = 'Mars' #為public屬性-> 所有instance都可以訪問

    #在class中也可以定義函數，稱為Method
    #這些方法可以通過該class的所有instance來訪問
    def say():
        print('hello world!')
    
    def say(self): 
        # 方法每次被調用，interpreter都會自動傳遞第一個實參
        # print self和object出來看，會看到是一樣的object
        # 也就是說這個參數，就是調用方法的object自己
        #  - 如果是p1調用的，則第一個參數就是p1本身
        #  - 如果是p2調用的，則第一個參數就是p2本身
        # 一般都會把這個參數name after "self"

        #在method當中不能直接訪問class中的屬性
        print('hello!')
        #print(name) #這樣會Error => 因為訪問不到
        print(f'I am {self.name}')

p1 = Person()
p2 = Person()
#p1.say() 
#TypeError: say() takes 0 positional arguments but 1 was given
#這邊就是與method調用 和 function調用的區別
#在function調用：傳了幾個arguments，就會有幾個實際的參數
#但是在method調用，會默認傳遞一個arguments，所以在mehthod當中至少要定義一個形參
p1.say() # hello!


#instance為何能visit到class中的屬性和method?
#   - class中定義的屬性和method都是public，任何該class都可以訪問
#   - 屬性和method查找的flow:
#       當我們調用一個object的屬性時，interpreter會先在當前對象中尋找是否含有該屬性
#       -> 如果有：則直接返回當前對象的屬性值
#       -> 如果沒有：則去當前對象的class object當中尋找，如果有，就返回class object，如果再沒有，就throw Error
p1.name = 'Max'
p2.name = 'Lisa'
print(p1.name) # Max
print(p2.name) # Lisa
#class object和instance當中都可以保存屬性、方法
#   - 如果這個屬性、方法是所有的instance共享的，則應該將其保存到class object當中
#   - 如果這個屬性、方法是某個instance特有的，則應該保存到instance當中, e.g.身高多少、體重多少

del p2.name
print(p2.name) # Mars


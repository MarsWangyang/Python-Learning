class Person:
    #name = 'Mars' #一般情況下不會直接定義屬性，因為大家的可能都會不一樣
    #這樣的name會是在class當中，只會出現一次
    def sayHello(self):
        print(f'hello! My name is {self.name}')

#以下列code為例，對於Person來說name是neccessary的，並且每一個object中的name屬性都是不同的
#目前是以name定義在object以後，並且手動添加進入object
#這種方式很容易出現錯誤
#在此我們的目標：希望object創建的時候，必須設定name，如果不設定object則不建構
#並且在創建name的時候應該是自動完成，而不是在創建object之後，才手動完成加入屬性
p1 = Person()
p1.name = 'Mars'

p2 = Person()
p2.name = 'MAX'

p3 = Person()
#p3.sayHello() =>因為沒有name的指定，所以會Throw Error出來


#在class當中可以定義一些魔術方法(特殊methods)
#特殊方法都是以__開頭，__結尾的方法
#特殊方法不需要自己調用(p.methods)，不要嘗試去掉用特殊方法
#特殊的方法會在特殊的時刻自動被interpreter調用
#學習方式：
#   1. 特殊方法什麼時候調用
#   2. 特殊方法有什麼用

#創建object的流程：
# 1. 創建一個variable
# 2. 在memory當中創建一個新的object
# 3. 執行class的code block中的code(只在class定義的時候執行一次)
# 4. __init__(self)方法執行
# 5. 將object id賦值給

class Person:
    print('Person code block中')
    def __init__(self, name):
        #init會在創建對象以後立刻執行
        #有什麼用？
        #可以用來向新創建的object中初始化屬性
        #通過self向新建的object初始化屬性
        #調用class創建object的時候，class後面的所有參數會依序傳入
        self.name = name #這種方式是在instance當中，並且把variable傳進來
        print('init method執行')

    def sayHello(self):
        print(f'Hello! My name is {self.name}')

p1 = Person('Lita')
# Person code block中
# init method執行
print(p1.name)

print('-'*20)

p2 = Person('Mars')
print(p2.name)

class Dog:
    '''
        狗的class
    '''

    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age 
        self.gender = gender
        self.height = height
    
    def bark(self):
        print(f'{self.name} is barking!')
    

d = Dog('Max', 2, 'male', 10)
d.bark()
#目前我們可以直接通過object.field的方式來修改屬性的value
#導致object中的屬性可以隨意修改 -> 非常不安全
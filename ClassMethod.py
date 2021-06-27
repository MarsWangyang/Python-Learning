#class method是一種可以不用instantiate就可以被調用的method，
#有點類似static method，不過，static method只能知道他自己的那個method，沒辦法在static中調用其他function(就像是function call一樣，沒有self參數)，
#但是class method可以調用class中的其他方法來使用，輸入的參數會是cls，表示沒有被instantiate的class本體
class A(object):
    # 属性默认为类属性（可以给直接被类本身调用）
    num = "类属性"

    # 实例化方法（必须实例化类之后才能被调用）
    def func1(self):  # self : 表示实例化类后的地址id
        print("func1")
        print(self)

    # 类方法（不需要实例化类就可以被类本身调用）
    @classmethod
    def func2(cls):  # cls : 表示没用被实例化的类本身
        print("func2")
        print(cls)
        print(cls.num)
        cls().func1()


#A.func1() #这样调用是会报错：因为func1()调用时需要默认传递实例化类后的地址id参数，如果不实例化类是无法调用的
A.func2()

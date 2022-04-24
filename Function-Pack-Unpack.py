#Function也是一個對象
#對象：memory中專門用來儲存數據的一塊區域

def fn():
    print('hello world')
print(fn) # <function fn at 0x105994040> => memory位置

def sum(a, b=2, c=10):
    print(f'{a} + {b} + {c} = {a+b+c}')

sum(1, c=30) #不能寫成sum(c=10, 1) -> 會需要依照順序撰寫

# Function在調用的時候，interpreter不會檢查parameter的類型
# 因此parameter可以傳遞任何類型的對象


#在函數當中對local variable重新賦值，不會影響其他變量
def fn1(a):
    a = 200
    print(f'a = {a}')
c = 10
fn1(c) # a = 200
print(c) #10
#=>以上因為a是形式參數，會直接修改變量

#如果是在function中修改一個對象
#那麼就會影響到所有指向該對象的variable
def fn2(a):
    a[0] = 30
    print(f'a = {a}') 
    print(f'id(a) = {id(a)}')
c = [10, 20, 30]
fn2(c) #a = [30, 20, 30]
print(f'c = {c}') # c = [30, 20, 30]
print(f'id(c) = {id(c)}')

#所以應該要傳進去一個copy，而不是直接傳list進入
#用shallow copy
b = [10, 20, 30]
fn2(b.copy())
#也可以用fn2(b[:])
print(f'b = {b}') # c = [10, 20, 30]
print(f'id(b) = {id(b)}')


# 不定長度的參數 
#以這樣的形式會是傳入一個tuple進入function內部
#會接收所有的positional parameter
def sum(*a):
    #定義一個弼亮，來保存結果
    result = 0
    for i in a:
        result += i
    print(result)
sum(123,345,213) #681

#帶星號的刑參只能有一個
#第一個給參數a, 第二個給參數b, 剩下的都保存到c的tuple當中
def fn3(a, b, *c):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
fn3(1,2,3,4,5,6) 
# a = 1
# b = 2
# c = (3, 4, 5, 6)


#可變參數不一定要寫在最後面，但是帶*參數後面的所有參數，都必須要加關鍵字
def fn4(a, *b, c):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
fn4(1,2,3,4,c=5)
# a = 1
# b = (2, 3, 4)
# c = 5

def fn5(*a, b, c):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
fn5(1,2,3,b=4,c=5)
# a = (1, 2, 3)
# b = 4
# c = 5


#如果在形參的開頭直接寫一個*，則要求所有的參數都必須要加入關鍵字才能傳入
def fn6(*, a, b, c):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
fn6(a=3,b=4,c=5)
# a = 3
# b = 4
# c = 5

# *形參只能接受positional parameters，不能接收關鍵字參數
#def fn3(*a):
#   print(f'a = {a}')
#fn3(b=1,d=2,c=3) => Error


# **形參可以接受其他關鍵字參數，並且會將這些參數統一保存到一個dictionary當翁
# **形參只能有一個，並且必須寫在所有參數的最後面！
def fn7(**a):
    print(f'a = {a}, type = {type(a)}')
fn7(b=1,d=2,c=3) 
# a = {'b': 1, 'd': 2, 'c': 3}, type = <class 'dict'>

def fn8(a, b, **c):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')

fn8(1, 2, c=3, e=10, f=20)
# a = 1
# b = 2
# c = {'c': 3, 'e': 10, 'f': 20}

#函數的unpack
def fn9(a,b,c):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
t = (10,20,30)
fn9(*t) #傳遞實參實，也可以在序列類型的參數中添加星號，這樣會自動將序列中的元素依序作為參數傳遞
#元素的個數必須看形參的個數一樣
# a = 10
# b = 20
# c = 30

# 創建一個字典
d = {'a':100, 'b':200, 'c':300}
#對字典unpakc (**來對dictionary做unpack)
fn9(**d)
# a = 100
# b = 200
# c = 300

#break -> 退出current loop
#contunue -> 跳到next loop
#return end up function

def fnHelp(a:int, b:bool, c:str='hello') -> str:
    '''
    這是一個文檔字符串的Example

    Function的作用：。。。。
    函數的para：
        a, 作用, 類型, 默認值。。。。。
        b, 作用, 類型, 默認值。。。。。
        c, 作用, 類型, 默認值。。。。。
    '''
    return a
help(fnHelp)
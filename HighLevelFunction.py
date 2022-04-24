#高階函數
#接收函數作為parameters, 或將function作為return value就是高階函數

#創建一個List
l = [i for i in range(1, 11)]

#定義一個函數，檢查任意數字是否是偶數
def Even(i):
    if i % 2 == 0:
        return True
    
    return False

#定義函數是否數字大於5
def BiggerThanFive(i):
    if i > 5 :
        return True
    return False

def fn(func, lst):
    '''
    fn() 可以將指定列表中的數字，根據傳入的function來做該動作
    
    para:
        lst: 要進行動作的list
    '''

    #創建一個新list
    newList = []

    #篩選內容物
    for i in lst:
        if func(i):
            newList.append(i)
    
    return newList

def FactoryThree(i):
    return i % 3 == 0


print(fn(FactoryThree, l))
print('-'*20)
print(fn(Even, l))
print('-'*20)
print(fn(BiggerThanFive, l))
print('-'*20)
#這樣就可以依據傳入的function來做內部的運作 -> 但還是有點麻煩會需要根據要什麼樣的方式去寫functions
#因此用filter()來使用

#filter(): 可以list中過濾出符合條件的元素，保存到一個新的list當中
#paras:
# 1. function: 根據該function來filter list
# 2. 需要filted的list
#Return values:
# filted list (Iterable object)
#！！！是傳function，而不是調用function，因此不可以寫funciton()，需要把括號給去除
result = filter(BiggerThanFive, l) #會在需要用list來轉換我們的iterable obejcts
print(list(result))

#以上還是一樣沒辦法改變function在global當中 -> 因此採用Lambda()匿名函數來創建function
# lambda用來創建簡單的function
print(lambda a, b: a + b) # <function <lambda> at 0x1029b6430>
print('-'*20)
result = filter(lambda i: i % 3 == 0, l) #使用完就會自己銷毀，從memory中是放掉
print(list(result))
print('-'*20)

#map()
#map(): 可以對iterable object中的所有elements做assigned operation，然後將其添加到一個新的object中
l = [n for n in range(1, 11)]
result = map(lambda i: i + 1, l)
print(list(result)) #[2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 
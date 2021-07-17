# 作用域(scope)
# 作用域指的是variable生效的區域

def fn():
    a = 10
    print(f'函數內部：{a}')
a = 100
fn()
print(f'函數外部：{a}')

#在python中有兩種作用域
# global scope: 在process創建時被創建，process結束就被銷毀(所有函數以外的區域都是global variable)
#   - 可以在任意的位置被visited
# local scope:
#   - 在函數被調用的時候作用，調用結束就銷毀
#   - 每調用一次就會產生一次函數作用域
#   - 只能在函數內部被visited

def fn2():
    a = 30

    def fn3():
        print(f'fn3中: a = {a}')
    fn3() #step2. fn3中: a = 30
fn2() #step1.
#以上的話就是：最內部的function可以往外看到最外面的function以及所有變量，但是外部的變量/function沒辦法看到inner 
#但是還是會優先尋找自己function中尋找variable，如果有就使用，如果沒有就往upper level scope去尋找

#在function中想修改global variable，必須要用keyword: global
v = 10
def fn4():
    global v #將function內的variable宣告其實是外部的全局變量
    v = 20
    print(f'函數內部: v = {v}')

fn4()
print(f'函數外部: v = {v}')
# 函數內部: v = 20
# 函數外部: v = 20

#namespace(就是變量儲存所在的位置，每一個variable都需要儲存到指定的namespace當中)
#每一個scope都會有一個對應的namespace

#locals(): 用來獲取當前作用域的namespace
# 如果在全局作用域中調用locals()，則獲取global namespace
# 如果在functional scope當中調用locals()，則獲取functional namespace

q = 10
scope = locals()
print(scope)
print(type(scope))
print(scope['q'])

scope['w'] = 10000 #像字典中添加key-value在global中創建一個變量(不建議使用)
#print(scope)

def fn11():
    e = 10
    scope = locals()
    print(f'scope: {scope}')

#global(): 可以在任意位置獲取全局namespace
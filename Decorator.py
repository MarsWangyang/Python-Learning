

def add(a, b):
    '''
        求任意兩個數的和
    '''
    return a + b

def mul(a, b):
    '''
        求任意兩個數的積
    '''
    return a * b

#希望函數能在計算前print：開始計算，計算結束後print:計算完畢
#如果可以直接修改函數中的code，會產生以下問題
# 1. 如果要修改的函數過多，修改起來會很麻煩
# 2. 對於後期維護非常麻煩和困難。
# 3. 如果函數是別人定義的，因此我們自己改不了，會違反開發原則：OCP
# OCP: 程式的設計，要求開發對程式的expand，要關閉對程式碼的修改
# 也就是不要去修改別人直接給你的code
# => 能否在不修改原函數的情況下，修改、擴展內容？


def fn():
    print('我是fn函數')

#只需要對現有的函數，來創建一個新的函數就可以
def fn2():
    print('函數開始執行')
    fn()
    print('函數執行結束')
fn2()


def new_add(a, b):
    print('函數開始執行')
    add(a, b)
    print('函數執行結束')
r = new_add(1,2)
print(r) #因為new_add是沒有return value => 因此接收到的只會是None
# => 這樣看不到結果

def new_add(a, b):
    print('函數開始執行')
    r = add(a, b)
    print('函數執行結束')
    return r
r = new_add(1,2)
print(r)
#這樣的確對我們的函數進行擴展，並且沒有影響到原code
#但是這個問題：如果要對100個函數擴展，那麼還是得去修改100個函數，並且很費工


#改 => 不要每次都手動創建新的函數
#現在：要創建一個函數，這個函數能夠可以自動地幫助生產函數

def begin_end():
    '''
        用來對其他函數進行擴展，使其他函數可以在執行前print開始執行，執行後print執行結束
    '''
    
    def new_function():
        print('開始執行')
        #調用被擴展的function
        #fn() #但這樣就又寫死了，這裡是不確定的function會傳入
        print('執行結束')

    return new_function
f = begin_end()
f2 = begin_end() 
print(f) #<function begin_end.<locals>.new_function at 0x106b3e700>
print(f2) #<function begin_end.<locals>.new_function at 0x106b3e790>\

# 改：讓各種function都可以進來
def begin_end(old):
    '''
        用來對其他函數進行擴展，使其他函數可以在執行前print開始執行，執行後print執行結束
        參數：
            old 要擴展的函數對象
    '''
    
    def new_function(a, b):
        print('開始執行')
        #調用被擴展的function
        r = old(a, b)
        print('執行結束')
        return r
    return new_function
f = begin_end(add)
r = f(1,2)
print(r) 
# 開始執行
# 執行結束
# 3


#以上會因為參數的個數不同，導致每次都會需要需改，要適應於所有參數的方式
def begin_end(old):
    '''
        用來對其他函數進行擴展，使其他函數可以在執行前print開始執行，執行後print執行結束
        參數：
            old 要擴展的函數對象
            *args: 
            **kargs: 接收所有的關鍵字參數，有就接收，沒有就不接收
    '''
    
    def new_function(*args, **kwargs):
        print('開始執行')
        #調用被擴展的function
        r = old(*args, **kwargs)
        print('執行結束')
        return r
    return new_function
f = begin_end(add)
r = f(1,2)
print(r) 
# 開始執行
# 執行結束
# 3
#把begin_end()這種還稱為裝飾器
#透過裝飾氣，可以在不修改原來函數的情況之下對函數進行擴展
#在開發中，我們都是透過裝飾器來擴展函數的功能


#但其實還是不是以上的用法，而是用@來裝飾
#定義函數時，可以通過@ decorator來指定裝飾器
#並且可以同時為一個function加裝多個decorators
@begin_end
def say_hello():
    print('Hello World')
say_hello() #現在已經是被begin_end裝飾過後的say_hello
# 開始執行
# Hello World
# 執行結束

#問題來了：多個裝飾器的輸出順序為何？
#函數按照由內向外的順序裝飾
def begin_end_fn3(old):
    '''
        用來對其他函數進行擴展，使其他函數可以在執行前print開始執行，執行後print執行結束
        參數：
            old 要擴展的函數對象
            *args: 
            **kargs: 接收所有的關鍵字參數，有就接收，沒有就不接收
    '''
    
    def new_function(*args, **kwargs):
        print('fn3裝飾：開始執行')
        #調用被擴展的function
        r = old(*args, **kwargs)
        print('fn3裝飾：執行結束')
        return r
    return new_function

@begin_end
@begin_end_fn3
def say_hello():
    print('你好')
say_hello() #函數按照由內向外的順序裝飾
# 開始執行
# fn3裝飾：開始執行
# 你好
# fn3裝飾：執行結束
# 執行結束
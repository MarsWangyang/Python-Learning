#將函數作為retuen value返回
#此種函數稱為closure, 通過此可以創建一些只有當前函數能夠訪問的變量
#可以將一些private的數據藏到closure當中
#形成Closure的條件：
#   1. function loop
#   2. 將內部函數作為return value
#   3. 內部函數必須要使用到外部函數的variable

def fn():
    a = 100 #現在只有r()能看到，誰也看不見，除了目前的inner可以看到

    #函數內部再定義一個function
    def inner():
        print('我是inner function')
    
    #將內部函數inner作為return value
    return inner

#r是一個函數，是調用fn()後返回的函數
#這個函數是在fn()內部定義的，並不是global function
#所以這個function總是可以訪問到fn()內的variable
r = fn()
print(r) #<function fn.<locals>.inner at 0x104ad24c0>
r() #我是inner function


#求平均值
nums = []

#創建一個函數，計算平均值
def avg(n):
    nums.append(n)
    return sum(nums)/len(nums)
#但這樣會被別人給修改到


#改
def make_avg():
    nums = []
    #創建一個函數，計算平均值
    def avg(n):
        nums.append(n)
        return sum(nums)/len(nums)
    return avg

avg = make_avg() 
print(avg(10))
print(avg(20))
print(avg(30))


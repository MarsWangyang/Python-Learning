#Set只能儲存不可變對象
#不會出現重複elements
#儲存的對象會是沒有順序的

s = {1, 2, 3, 4, 4, 3, 4}
#s = {[1, 2, 3], [4, 5, 6]} #在set當中不能放可變變量 -> TypeError
print(s, type(s))

s = {} #這樣會是一個dictionary
s = set() #這樣才會是一個空集合
#可以通過set()將list或是dictionary轉換成為集合
s = set([1,2,3,4,5,6,4,3,3,2])
print(s, type(s)) #{1, 2, 3, 4, 5, 6} <class 'set'>
s = set('hello')
print(s, type(s)) #{'l', 'h', 'o', 'e'} <class 'set'>

#將dictionary轉換成為集合，只會保存key轉換成為集合
s = set({'name':'Mars', 'age':18})
print(s, type(s)) #{'name', 'age'} <class 'set'>
#沒辦法通過index來操作set，只能先轉換成為list才能做index操作


#len()來獲取集合數量，in是看是否elements有在set當中
s = {1,2,3,4}
print(1 in s) #True
print(len(s)) #4

#利用add()對set添加elements
s = set()
s.add(1)
print(s) #{1}

#update()將一個集合中的元素加入當前集合中
s2 = set('hello')
s.update(s2)
s.update((10,20,30))
print(s) #{1, 'l', 'e', 10, 20, 'o', 'h', 30}

s.update({10:'lol', 20:'he'})
print(s) #{1, 'l', 10, 'h', 20, 'o', 30, 'e'}

#pop() -> 是隨機的pop，而不是從最後的，因為我們無法控制set中的順序
result = s.pop()
print(result)

#remove -> 刪除指定的element
s.remove(10)
print(f's: {s}') #s: {'l', 'h', 20, 'o', 'e', 30}

#clear()清空集合
s.clear()
print(s) #set()

#copy()對集合進行shallow copy

# set operation
s = {1, 2, 3 , 4, 5}
s2 = {3,4,4,5,6}
result = s & s2 #交集
print(result)

# | Union
result = s | s2
print(result)

# - 差集
result = s - s2
print(f'result = {result}')

# ^ XOR 只在一個集合中出現的elements
result = s ^ s2
print(result)

# <= 檢查一個集合是否是另一個集合的subset
#如果一個集合中的元素全部都在另一個集合當中出現
#那麼這個集合就是另一個集合的子集合
a = {1,2,3}
b = {1,2,3,4}
print(a <= b) #True

result = {1,2,4} <= {1,2,3,4}
print(result) #True

# < 檢查一個集合是否是另一個集合的超子集
# 如果超集b中含有子集a中的所有元素，並且b中還有a中沒有的元素
# 則b就是a的真超集，a就是b的真子集
result = {1,2,3} < {1,2,3}
print(result) #False
result = {1,2,3} < {1,2,3,4} 
print(result) #True

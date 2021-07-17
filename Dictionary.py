#Dictionary
#資料結構為mapping
#list儲存的性能很好，但是在查詢的時候性能很差
#每個element都只有唯一的一個名字，通過這個唯一的名字來找到指定的元素
#唯一的名字：key
#對象：value
#key-value 結構
#每個字典都可以有多個key-value，而每一對key-value都是一個item

d = {}
print(d, type(d))

d = {'name':'孫悟空', 'age':18, 'gender':'male'}
#字典的value可以是任何對象
#key則是任意的不可變對象(e.g. int, str, bool, tuple...)
#字典的key是不能重複的如果出現，後面的會替換成為前面的override
print(d, type(d))
print(d['name'])
#print(d['hello'])

dd = dict(name='孫悟空', age=18, gender='男') #每個parameter都是key-value
print(dd, type(dd)) #{'name': '孫悟空', 'age': 18, 'gender': '男'}

ddd = dict([('name', '孫悟空'), ('age', 18)])
print(ddd) #{'name': '孫悟空', 'age': 18}
print(len(ddd)) #2


# in 檢查文件當中有沒有包含該key
print('hello' is d) # False
print('hello' is not d) # True

#獲取值
print(ddd['name']) # 孫悟空
#如果利用[]來獲取值時，沒有這樣的key，會return KeyError

#get利用key來獲取value
print(ddd.get('name')) #孫悟空
print(ddd.get('hek')) #None  -> 不會throw Error，而是會return KeyError
print(ddd.get('hello', 'Default Value')) #Default Value -> 指定默認值


#修改
ddd['name'] = '豬八戒'
print(ddd.get('name')) # 豬八戒

ddd['address'] = '花果山'
print(ddd) # 如果key doesn't exist -> 會添加


#設定返回值
#如果key存在在dictionary當中，則返回key的value
#如果key不存在在dictionary當中，則返回我們自己設定的default value
result = ddd.setdefault('name', '唐三藏')
print(f'result = {result}') #豬八戒

#將其他dictionary中的key-value添加到目前的dictionary當中
#如果有重複的key，則會將其他的dictionary中的key-value替換掉當前的key-value
d = {'a':1, 'b':2, 'c':3}
d2 = {'d':4, 'e':5, 'a':7}
d.update(d2)
print(d) # {'a': 7, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


#刪除dictionary中的items
del d['a']
del d['b']
print(d) #{'c': 3, 'd': 4, 'e': 5}

#popitmem()
#return 會返回tuple, 第一個會是key, 第二個會是value
result = d.popitem()
print(f'result = {result}, d = {d}') # result = ('e', 5), d = {'c': 3, 'd': 4}

#pop()可以多選擇key去刪除
#如果刪除不存在的key => 會throw KeyError, 可以指定default value
result = d.pop('d')
print(f'result = {result}, d = {d}') # result = 4, d = {'c': 3}

result = d.pop('z', 'default')
print(result) #default

#clear()刪除所有的items
d.clear()
print(d) #{}

#copy()
#會對dictionary做shallow copy -> !!shallow copy: 只會複製對象裡面的value，如果value也是可變對象，那麼就不會被複製
d = {'a':1, 'b':2, 'c':3}
d2 = d
#d, d2都是指向同一個對象 -> 因此修改一個會影響到另一個
d3 = d.copy()
d['a'] = 100

print(f'd = {d}, d_id = {id(d)}')    # d = {'a': 100, 'b': 2, 'c': 3}, d_id = 4425498112
print(f'd2 = {d2}, d2_id = {id(d2)}')# d2 = {'a': 100, 'b': 2, 'c': 3}, d2_id = 4425498112
print(f'd3 = {d3}, d3_id = {id(d3)}')# d3 = {'a': 1, 'b': 2, 'c': 3}, d3_id = 4425423424


d = {'a':{'name':'孫悟空', 'age':18}, 'b':2, 'c':3} #因為a中的value是一個可變對象，因此shallow copy還是指向同一個reference
d2 = d.copy()
d['a']['name'] = '豬八戒'
print(f'd = {d}, d_id = {id(d)}')    # d = {'a': {'name': '豬八戒', 'age': 18}, 'b': 2, 'c': 3}, d_id = 4524382336
print(f'd2 = {d2}, d2_id = {id(d2)}')# d2 = {'a': {'name': '豬八戒', 'age': 18}, 'b': 2, 'c': 3}, d2_id = 4524389568
#deepcopy少用->因為會影響效能


# Traversal keys(), values(), items()
# keys() -> return all keys in dict(),會返回list

d = {'name':'Mars', 'age':18}
print(d.keys()) #dict_keys(['name', 'age'])
for i in d.keys():
    print(i, d[i]) 

#values() -> retual all values in dict()
for v in d.values():
    print(v) 

#items() -> retual all items in dict()
#return a list，包含雙值子序列
print(d.items()) #dict_items([('name', 'Mars'), ('age', 18)])
for k, v in d.items():
    print(k, v)



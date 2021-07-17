#每個對象中都保存了三個數據： 也就是說每個variable會存一個reference(也就是存memory中的地址)
# id(reference位置)      會經過調用reference過後，到memory中才會真正地看到我們的value
# Type
# value
#List就是一個可變對象: a = [1, 2, 3]

a = [1, 2, 3]
a[0] = 10   #為修改一個對象，現在這樣就是通過variable，
            #找到了reference在memory中的位置
            #去修改了memeory中a[0]的value
            #因此不會改變variable的reference
            #若有其他variable也指向這個reference，那麼值也會改變
a = [3,4,5] #這樣的方式會是改variable
            #這樣就會在memory當中又創建了一個object
            #並且把我們variable的reference指向到了現在在memory中創建的address
            #會改變variable的reference
            #為一個variable重新賦值時，不會影響到其他的variable

aa = [1,2,3]
print(f'修改前: {aa}, id: {id(aa)}') #修改前: [1, 2, 3], id: 4457369984

aa[0] = 13
print(f'修改前: {aa}, id: {id(aa)}') #修改前: [13, 2, 3], id: 4457369984

aa = [3,4,5]
print(f'修改前: {aa}, id: {id(aa)}') #修改前: [3, 4, 5], id: 4457369728


bb = [1,2,3]
c = bb
print(f'修改前bb: {bb}, id: {id(bb)}')#修改前bb: [1, 2, 3], id: 4427395136
print(f'修改前c: {c}, id: {id(c)}')   #修改前c: [1, 2, 3], id: 4427395136
bb[0] = 321
print(f'修改後b: {bb}, id: {id(bb)}') #修改後bb: [321, 2, 3], id: 4427395136
print(f'修改後c: {c}, id: {id(c)}')   #修改後c: [321, 2, 3], id: 4427395136


# ==, !=: 是比較variable的value是否一樣
# is, is not: 是比較variable的id是否一樣 => 也就是reference(address)是否相同

a = [1, 2, 3]
b = [1, 2, 3]
print(a, b) # [1, 2, 3] [1, 2, 3]
print(id(a), id(b)) # 4438424448 4438434432
print(a == b) #True  =>問value是否一樣
print(a is b) #False =>問address是否一樣


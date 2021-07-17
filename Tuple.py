#tuple是一個不可以變的數列
#操作和list是一樣的，當作不可以變的list就可以了

myTuple = ()
print(myTuple, type(myTuple)) #() <class 'tuple'>

myTuple = (1,2,3,4,5)
print(myTuple[3]) #4
#myTuple[3] = 10 #這邊會出錯，因為tuple是不能被改變的

#Tuple不是null時，括號可以省略
#如果tuple is not null，裡面至少要有一個element
myTuple = 10,20,30,40
print(myTuple, type(myTuple)) #(10, 20, 30, 40) <class 'tuple'>

#tuple的unpack
#unpack就是說將tuple中的每一個元素都賦值給一個variable
#對一個tuple進行unpack時，variable數量必須和tuple中的elements數量一樣
#如果不想要把所有variable都寫出來，可以在variable前面放一個*，就會把所有剩下元素都給此變數
#但是不同出現兩個或兩個以上的* -> Error
#其實不是只有能對tuple做unpack，對String, list也可以unpack
myTuple = 10, 20, 30, 40
a, b, c, d = myTuple
print(f'a = {a}') # a = 10
print(f'b = {b}') # b = 20
print(f'c = {c}') # c = 30
print(f'd = {d}') # d = 40
#所以兩個值的交換：其實就是利用tuple來做unpack的動作
a, b = b, a
print(a, b) # 20 10
a, b, *c = myTuple 
print(a, b) # 10 20
print(c) # [30, 40]
*a, b, c = myTuple
print(a, b, c) # [10, 20] 30 40

myList = [1,2,3,4,5,6]
a, *b, c = myList
print(a, b, c) # 1 [2, 3, 4, 5] 6
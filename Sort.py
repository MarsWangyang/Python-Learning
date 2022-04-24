#sort()
#該方法用來對List當中的elements進行排序
#在sort()可以接收一個keyword: key
#   - key需要一個函數作為參數
#   - 每次都會以列表中的一個元素作為參數來調用該函數，並且使用函數的return value來比較元素的大小
l = ['bb', 'aaa', 'c']
l.sort(key=len)
print(l) # ['c', 'bb', 'aaa']

l = [3,6,1,2,'5', "9"]
l.sort(key=int)
print(l) #[1, 2, 3, '5', 6, '9']

#sorted()
#這個函數和sort()的用法一樣，但是sorted可以對任意的list進行排序
#並且使用此function排序不會影響原來的對象，而是會return一個新的object
l = [2,3,8,6,'5','4']
print(f'排序前： {l}') #排序前： [2, 3, 8, 6, '5', '4']
print(sorted(l, key=int)) #[2, 3, '4', '5', 6, 8]
print(f'排序後： {l}') #排序後： [2, 3, 8, 6, '5', '4']

l = '132135431215484984'
print(sorted(l)) #['1', '1', '1', '1', '2', '2', '3', '3', '3', '4', '4', '4', '4', '5', '5', '8', '8', '9']


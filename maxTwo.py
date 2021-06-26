def MaxTwoWithoutSorted(userList):
    userList = list(map(int ,userList))
    m1, m2 = (userList[0], userList[1]) if userList[0] > userList[1] else (userList[1], userList[0])

    for i in range(2, len(userList)):
        if userList[i] > m1:
            m2 = m1
            m1 = userList[i]
        elif userList[i] > m2:
            m2 = userList[i]
    return m1, m2

def MaxTwoSorted(userList):
    userList = sorted(list(map(int ,userList)))
    m1, m2 = userList[-1], userList[-2]
    return m1, m2

if __name__ == '__main__':
    userList = input('輸入一個串數字，用空格間隔: ').split()
    print(f'Max values: {MaxTwoWithoutSorted(userList)[0]}, Second Max values: {MaxTwoWithoutSorted(userList)[1]}')
    print(f'Max values: {MaxTwoSorted(userList)[0]}, Second Max values: {MaxTwoSorted(userList)[1]}')

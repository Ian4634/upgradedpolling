a = ['ian', 'eason']
b = [0]


def compare(long, shortList):
    dif = long-len(shortList)
    for i in range(dif):
        print(i)
        shortList.insert(0, 'none')
    return shortList


if __name__ == '__main__':
    compare()

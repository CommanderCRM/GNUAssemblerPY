import dis


def posArray(a, b):
    posSum = 0
    i = [10, 50, -30, 300, 350, 900, -50, -100, -500]
    for k in range(9):
        if a <= i[k] <= b and i[k] > 0:
            posSum = posSum + i[k]
    print(posSum)


posArray(300, 390)
dis.dis(posArray)

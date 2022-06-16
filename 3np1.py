#https://onlinejudge.org/external/1/100.pdf

lenghtOfNums = {1: 1}


def problemFunc(n):
    if lenghtOfNums.get(n, 0) == 0:
        if n % 2 == 1:
            lenghtOfNums[n] = 1 + problemFunc(3 * n + 1)
        else:
            lenghtOfNums[n] = 1 + problemFunc(n / 2)
    return lenghtOfNums.get(n, 0)


pairs = []
listOfNum = list(map(int, input().split()))
while listOfNum:
    if len(listOfNum) != 2 or listOfNum[0] <= 0 or listOfNum[1] <= 0 or listOfNum[0] > listOfNum[1]:
        break
    pairs.append(listOfNum)
    listOfNum = list(map(int, input().split()))

for numOfPair in pairs:
    maxInPair = 0
    for i in range(numOfPair[0], numOfPair[1] + 1):
        temp = problemFunc(i)
        if maxInPair < temp:
            maxInPair = temp
    print(numOfPair[0], " ", numOfPair[1], " ", maxInPair)

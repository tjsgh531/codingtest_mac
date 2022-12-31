def solution(arrayA, arrayB):
    maxdivA = maxdvision(arrayA)
    maxdivB = maxdvision(arrayB)
    if maxdivA > maxdivB:
        for i in arrayB:
            if i % maxdivA == 0:
                return 0
        return maxdivA
                
    else:
        if maxdivB == 1:
            return 0

        for i in arrayA:
            if i % maxdivB == 0:
                return 0
        return maxdivB


def maxdvision(array):
    minval = min(array)
    for i in range(minval, 0, -1):
        for j in array:
            if j % i != 0:
                break
        else:
            return i

arrayA = [10, 20]
arrayB = [5, 17]
print(solution(arrayA, arrayB))
        

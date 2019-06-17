def logenstCollatzSequenz(number):
    result = 0
    maxChain = 0
    for i in range(2,number):
        chainNumber = i
        sumChain = 0
        while True:
            if chainNumber == 1:
                if sumChain > maxChain:
                    result = i
                    maxChain = sumChain
                break
            if chainNumber%2 == 0:
                chainNumber = chainNumber/2
                sumChain += 1
            elif chainNumber%2 != 0:
                chainNumber = chainNumber*3 + 1
                sumChain += 1

    return result, maxChain

print(logenstCollatzSequenz(1000000))

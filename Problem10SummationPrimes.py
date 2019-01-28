def primeSum(rangeSum):
    sum = 0
    for i in range(2,rangeSum):
            for y in range(2,i+1):
                if (y * y) > i:
                    sum +=i
                    break
                if i%y == 0:
                    break



    return sum

print(primeSum(2000000))

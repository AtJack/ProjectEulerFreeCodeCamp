def primeCounter(count):
    x = 1
    y = 1
    while x < (count):
        y += 1
        for z in range(2,y):
            if (z*z) > y:
                x += 1
                result = y
                break
            if y%z == 0:
                break

    return result

print(primeCounter(10001))

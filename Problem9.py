for c in range(1,999):
    for b in range(1,1000):
        if b > c:
            break
        for a in range(1,1000):
            if a > b or (a+b+c) > 1000:
                break
            if (a+b+c) == 1000 and (a**2+b**2)== c**2:
                print(a,b,c)
                break

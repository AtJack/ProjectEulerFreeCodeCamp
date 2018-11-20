numDigits = 3
palin = 0
i = 0
x = 0

for i in range(int("1" * numDigits),int("9"*numDigits)+1,1):
    for x in range(int("1" * numDigits),int("9"*numDigits)+1,1):
        if str(i*x) == str(i*x)[::-1]:
            if i*x > palin:
                palin = i * x

print(palin)

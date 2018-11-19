result = 0
x = 1
y = 2

while y < 4000000:
    if y%2 == 0:
        result += y
    y += x
    x = y - x

print(result)

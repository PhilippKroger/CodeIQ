for x in range(0, 1000):
    for y in range(0, 1000):
        x1 = x
        y1 = y
        s = (x1+y1)/2
        if x1>s:
            if x1>y1:
                x1 = x1-y1
            else:
                x1 = y1 - x1
        else:
            z = s * x + y
            if z==265:
                print(z, x, y)

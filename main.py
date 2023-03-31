def factorial(x):
    y = x
    for i in range(1, x):
        y = y * (x-i)
    
    return y
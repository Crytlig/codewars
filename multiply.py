def mult(*args):
    result = 1
    try:
        for num in args:
             result *= num
        return int(result)
    except ValueError:
        return "Not a number"
print(mult(1,3))

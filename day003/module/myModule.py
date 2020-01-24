#myModule

def sum(a, b):
    return safe_sum(a, b)

def real_sum(a, b):
    return a + b

def safe_sum(a, b):
    if(type(a) != type(b)):
        print("cause of type mismatch, can't do that")
        return
    else:
        result = real_sum(a, b)
        return result

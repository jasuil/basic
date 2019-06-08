#closure

def outer():
    msg = "hi"

    def inner():
        print(msg)

    return inner


h = outer()

h()


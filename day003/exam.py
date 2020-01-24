# fibonnachi

def fibonnich(n):
    start = 0
    next = 1
    sum = 0


    if n <= 0:
        pass


    sum = start + next
    start = next
    next = sum

    n -= 1

    fibonnich(n)




fibonnich(3)

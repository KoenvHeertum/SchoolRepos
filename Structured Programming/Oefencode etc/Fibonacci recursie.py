def fibr(n):
    if n < 2:
        return 1
    return fibr(n-1) + fibr(n-2)

fibr(9)
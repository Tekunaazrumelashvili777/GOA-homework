def max_of_three(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)
print(max_of_three(3, 7, 5))  
print(max_of_three(10, 2, 10)) 
print(max_of_three(-1, -5, -3))
def fibonacci_recursive(n):
    
    if n == 0 :
        return 0

    elif n == 1:
        return 1

    else:
        return fibonacci_recursive(n -1) + fibonacci_recursive(n-2)  



for i in range(8):
    print(fibonacci_recursive(i), end=", ")  # 0, 1, 1, 2, 3, 5, 8, 13

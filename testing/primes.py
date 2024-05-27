def is_prime(n):
    if n<2:
        return False
    
    for num in range(2,n):
        if n%num == 0:
            return False
        
    return True
    
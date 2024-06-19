=======
def fibonacci(n):
    """
    Returns the nth Fibonacci number.
    
    Parameters:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The nth Fibonacci number.
    """
    a, b = 0, 1
    
    for _ in range(n):
        a, b = b, a + b
    
    return a
>>>>>>> REPLACE

def fibonacci(n):
    """
    Returns the nth Fibonacci number.
    
    Parameters:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 1:
            return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

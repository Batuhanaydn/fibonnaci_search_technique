"""
Bu algoritma geliştirilirken:
https://en.wikipedia.org/wiki/Fibonacci_search_technique
adresindeki bilgiler kullanılmıştır.
"""

from functools import lru_cache

def fibonacci(num: int) -> int:
 
    """
    >>> fibonacci(10)
    55
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    """
    
    if not isinstance(num, int):
        raise TypeError("Num must be an integer")
    if num < 0:
        raise ValueError("Num integer must be greater or equal to zero")
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def fibonacci_search(arr: list, val: int) -> int:
    
    """
    >>> fibonacci_search(list(range(-100, 100, 3)), -10)
    30
    """
    
    liste = len(arr)
    a = 0
    while True:
        if fibonacci(a) >= liste:
            fibo_a = a
            break
        a += 1
    level = 0
    while fibo_a > 0:
        index_a = min(
            level + fibonacci(fibo_a - 1), liste -1
        )
        item_a_1 = arr[index_a]
        if item_a_1 == val:
            return index_a
        elif val < item_a_1:
            fibo_a -= 1
        elif val > item_a_1:
            level += fibonacci(fibo_a -1)
            fibo_a -= 2
    else:
        return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # doctest.testmod sayesinde uygulamanızı sürekli olarak çağırmadan sürekli olarak test edebilirsiniz.


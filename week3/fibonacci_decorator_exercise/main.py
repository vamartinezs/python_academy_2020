from week3.fibonacci_decorator_exercise.decorators import fibonacci_decorator


@fibonacci_decorator
def fibonacci(n):
    """Based of the following fibonnaci declaration, create a decorator for caching the results"""
    if n <= 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(200)

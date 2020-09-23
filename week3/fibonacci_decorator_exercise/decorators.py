
def fibonacci_decorator(func):
    """Decorator for storing calculations applied of fibonacci function"""
    fibonacci_records = {}

    def fibonacci_wrapper(*args, **kwargs):
        """ args[0] stores the param from  fibonacci. We need it to evaluate if it's calculation is needed"""
        if args[0] in fibonacci_records:
            return fibonacci_records[args[0]]
        else:
            value = func(*args, **kwargs)
            print("fibonacci({}) = {}".format(args[0], value))
            fibonacci_records[args[0]] = value
            return value
    return fibonacci_wrapper


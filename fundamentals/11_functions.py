def hello(greet, name):
    print(f"Hello {greet} {name}")

hello("Good evening", "Daniel")

def big_function(*args, **kwargs):
    print(args, kwargs)
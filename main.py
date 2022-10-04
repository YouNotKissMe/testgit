


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}',1)  # Press Ctrl+F8 to toggle the breakpoint.


def new_func(func):
    def wrappler(a, b):
        if b > a:
            func(b, a)
        else:
            func(a, b)

    return wrappler






@new_func
def test(a, b):
    return print(a)


test(4, 5)



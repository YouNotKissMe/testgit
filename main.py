# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def new_func(func):
    def wrappler(a, b):
        if b > a:
            func(b, a)
        else:
            func(a, b)

    return wrappler


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


@new_func
def test(a, b):
    return print(a)


test(4, 5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

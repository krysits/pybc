from tests.validate import is_secure
from tests.example import run_example


def print_msg(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    is_secure()
    run_example()

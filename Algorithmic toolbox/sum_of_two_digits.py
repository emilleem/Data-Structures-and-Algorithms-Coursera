def sum(first, second):
    return first + second


if __name__ == '__main__':
    a, b = map(int, input("Enter two digits separated by a space: ").split())
    print(f"{a} + {b} = {sum(a, b)}")
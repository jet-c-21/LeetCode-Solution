def fun1(x):
    print('func1')
    return x


def fun2(x):
    print('func2')
    return x


if __name__ == '__main__':
    x = 1

    y = fun2(x) + fun1(x)

    print(y)

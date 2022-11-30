# coding: utf-8
"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 2022/11/29
"""


def fun(n):
    if n > 0:
        fun(n - 1)
        print(n)


if __name__ == '__main__':
    fun(3)

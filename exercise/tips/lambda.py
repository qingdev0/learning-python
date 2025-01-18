#!/usr/bin/env python3
##################################################################################################
# created    : 2021-11-25
# highlights : anonymous functions declared by lambda keyword
##################################################################################################


# The lambda keyword in Python provides a shortcut for declaring small and anonymous functions:

add = lambda x, y: x + y
add(5, 3)
8

# You could declare the same add() function with the def keyword:


def add(x, y):
    return x + y


add(5, 3)
8

# So what's the big fuss about?
# Lambdas are *function expressions*:
(lambda x, y: x + y)(5, 3)
8

# 1) Lambda functions are single-expression functions that are not necessarily bound to a name (they can be anonymous).
# 2) Lambda functions cannot use regular Python statements and always include an implicit `return` statement.

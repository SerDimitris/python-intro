# World
# W
# oo
# rrr
# llll
# ddddd

str = "World"

for i in range(len(str)):
    print(str[i] * (i + 1))


# Hello
# H***
# ee**
# lll*
# 0000

str = "Hello"


for j in range(len(str)):
    print(str[j] * (j + 1), end="*" * (len(str) - j - 1))
    print()
#!/usr/bin/python3

for c in reversed(range(97, 123)):
    if c % 2 == 1:
        c -= 32
    print(f"{chr(c)}", end="")

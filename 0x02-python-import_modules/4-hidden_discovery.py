#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    list = dir(hidden_4)
    n = len(dir(hidden_4))
    for i in range(n):
        if list[i][:2] != "__":
            print(list[i])

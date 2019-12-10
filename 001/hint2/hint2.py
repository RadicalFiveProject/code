#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Copyright (C) 2019 Ahirui Otsu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
from collections import Counter
import matplotlib.pyplot as plt

# Usage:
# ./hint2.py < cipher.txt

def main():

    n = 1

    cipher = ''.join(''.join(line.split()) for line in sys.stdin.readlines())
    c = [[] for i in range(n)]
    for i, e in enumerate(cipher):
        c[i % n].append(e)
    counters = [Counter(c[i]) for i in range(n)]
    for i, cnt in enumerate(counters):
        plt.figure(i)
        plt.title(f'{i}')
        k, v = zip(*cnt.most_common())
        s = sum(v)
        v = tuple(e / s for e in v)
        plt.bar(k, v)
    plt.show()

if __name__ == '__main__':
    main()

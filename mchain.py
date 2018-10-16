#!/usr/bin/env python3
import random
class markov:
    def __init__(self, stay, go, back):
        self.stay = stay
        self.go = go
        self.back = back
rain = markov(2, 4, 3)
clear = markov(3, 2, 1)
snow = markov(4, 2, 3)
def weatherchain(A, B, C):
    seed = random.randint(0,3)
    if seed == 1:
        print(A.stay)
        start = 0
    elif  seed == 2:
        print(B.stay)
        start = 1
    elif  seed == 3:
        print(C.stay)
        start = 2
    chain = [A, B, C]
    print(chain[start])

weatherchain(clear, rain, snow)

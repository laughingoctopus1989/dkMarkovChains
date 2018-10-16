#!/usr/bin/env python3
import random
class markov:
    def __init__(self, name, stay, go, back):
        self.name = name
        self.stay = stay
        self.go = go
        self.back = back
rain = markov("rain", 2, 4, 3)
clear = markov("clear", 3, 2, 1)
snow = markov("snow", 4, 2, 3)
def weathergen(A, B, C):
    chain = [[A.name, A.stay, A.go, A.back], [B.name, B.stay, B.go, B.back], [C.name, C.stay, C.go, C.back]]
    print(chain)
    random.shuffle(chain)
    print(chain)
weathergen(clear, rain, snow)

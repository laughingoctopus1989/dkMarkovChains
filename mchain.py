#!/usr/bin/env python3
import random
class markov:
#I decided to use classses with this because 1. it's a more convenient way to store information 2. I needed the practice
    def __init__(self, name, stay, go, back):
        self.name = name #name of the weather event
        self.stay = stay #chance for the weather event to repeat
        self.go = go #chance to go to the next weather event
        self.back = back #chance to go to repeat the last weather event
#this is just setting up the weather events
rain = markov("rain", 2, 4, 3)
clear = markov("clear", 3, 2, 1)
snow = markov("snow", 4, 2, 3)
#function used to generate the weather
def weathergen(A, B, C):
    chain = [[A.name, A.stay, A.go, A.back], [B.name, B.stay, B.go, B.back], [C.name, C.stay, C.go, C.back]]
    #I found out using multi-dimensiona arrays let me acces class data without screwing up the function and producing memory issues
    random.shuffle(chain)
    #this makes sure the starting pattern is random
    i = 0 #increment counter
    w = 0 #weather event
    e = 1 #weather event data
    print(chain) #prints the current chain info for debugging REMOVE LATER!!!
    while i != 7:
        if random.randint(0,chain[w][e]) == chain[w][e]: #checks to stay
            print(chain[w][0]) #prints current weather event
            i += 1
            random.shuffle(chain) # get rid of later!!!
        elif random.randint(0,chain[w][e+1]) == chain[w][e+1]: #checks to go
            print(chain[w+1][0]) #prints next weather event
            i += 1
            random.shuffle(chain) #get rid of later!!!
        elif random.randint(0,chain[w][e+2]) == chain[w][e+2]:
            print(chain[w+2][0]) #prints last weather event
            i += 1
            random.shuffle(chain) #get rid of later!!!
        else:
            random.shuffle(chain) #get rid of later!!!
weathergen(clear, rain, snow) #runs the fucntion lmao

import pandas as pd
import numpy as np
import pickle

ents = open('entlist.txt', 'rb')
entlist = pickle.load(ents)
targ = open('target.pkl', 'rb')
target = pickle.load(targ)
for y in entlist:
    


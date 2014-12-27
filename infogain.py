import pickle
import pandas as pd
import numpy as np


def calc_infogain():
    data = 'TRAIN_data2.csv'
    df = pd.read_csv(data)
    cols = df.columns
    input = open('entlist.pkl', 'rb')
    entlist = pickle.load(input)
    df = []
    target = 'Exacebator'
    skip = 'sid'
    print str(cols)
    print target
    print skip
    for x in cols:
        if x == 'sid':
            pass
        if x == 'Exacebator':
            pass
            # need to calculate the parent here. 
        else:
            entrop = entlist[x]
            pinp = open('codes'+x+'.pkl', 'rb')
            ps = pickle.load(pinp)
            for z in ps:
                

if __name__ == '__main__':
    calc_infogain()






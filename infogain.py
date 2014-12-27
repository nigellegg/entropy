import pickle
import pandas as pd
import numpy as np


def calc_infogain():
    data = 'TRAIN_data2.csv'
    df = pd.read_csv(data)
    cols = df.columns
    input = open('entlist.pkl', 'rb')
    entlist = pickle.load(input)
    input = open('parent_ents.pkl', 'rb')
    parent_ents = pickle.load(input)
    df = []
    target = 'Exacebator'
    skip = 'sid'
    print str(cols)
    print target
    print skip
    infogain = {}
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
            i = 0
            info = 0
            for a in parent_ents:
                info = info + a
            child = 0
            for z in ps:
                child = child + (z * entrop[i])
                i += 1
            info = infor - child
            infogain[x] = info
    output = open('infogain.pkl', 'wb')
    pickle.dump(infogain, output)
    output.close()
    print('Infogain for each variable is held in ')


if __name__ == '__main__':
    calc_infogain()

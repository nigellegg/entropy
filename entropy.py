import pandas as pd
import numpy as np
import pickle


def main():
    datfile = 'TRAIN_data2.csv'
    df = pd.read_csv(datfile)
    y = df.columns
    df = df.fillna(value=0)
    print y
    target = 'Exacebator'
    idvar = 'sid'
    entropy_list = []
    target_codes = []
    codelist = []
    entropy = {}
    for x in y:
        print x
        if x == idvar:
            pass
        elif x == target:
            target_ps = []
            target_codes = GetTarget(df, x)
            for a in target_codes:
                dx[df[target] == int(a)]
                l = len(dx)
                p = l/float(len(df))
                plog = (np.log(p))
                ent = p * plog
                target_ps.append(ent)
            output = open('parent_ents.pkl', 'wb')
            pickle.dump(target_ps, output)
        else:
            codelist = GetCodelist(df, x)
            # need to define the type of variable.
            if len(codelist) > 10:
                print 'recoding'
                max = df[x].max()
                min = df[x].min()
                med = df[x].median()
                m1 = med/2
                m2 = med + med/2
                i = 0
                while i < len(df):
                    df[x][i] = recode(df[x][i], m1, med, m2)
                    i += 1
                print df[x]
                codelist = GetCodelist(df, x)
            # entropy = - p1 log(p1) - p2 log(p2) - ...
            ent_tab = np.zeros((len(target_codes), len(codelist)))
            z = len(df)
            for a in target_codes:
                dx = df[df[target] == int(a)]
                i = 0
                codes = {}
                for y in codelist:
                    dy = dx[dx[x] == int(y)]
                    l = dy[x].count()
                    p = l/float(len(df))
                    print 'l = ', l
                    print 'len(df) = ', len(df)
                    print 'y = ', y
                    print 'p = ', p
                    codes[y] = p
                    plog = -(np.log(p))
                    print 'plog = ', plog
                    n = p*plog
                    print 'n = ', n
                    ent_tab[(int(a)), i-1] = n
                    i += 1
                out = open('codes'+x+'.pkl', 'wb')
                pickle.dump(codes, out)
                out.close()
            ents = []
            for a in target_codes:
                i = 0
                ents = []
                ent = 0
                while i<len(codelist):
                    ent = ent + ent_tab[(int(a)), i-1]
                    i += 1
                    ents.append(ent)
            entropy[x] = ents
            print str(entropy)
    out = open('entlist.pkl', 'wb')
    pickle.dump(entropy, out)
    out.close()
    print("All done")


def recode(x, m1, med, m2):
    if x == 0:
        x = 0
    if x < m1:
        x = 1
    if x > m1 and x < med:
        x = 2
    if x > med and x < m2:
        x = 3
    if x > m2:
        x = 4
    return x


def GetTarget(df, x):
    print 'Getting target'
    target_codes = []
    z = df.groupby(x).count()
    for y in z.index:
        target_codes.append(y)
    print str(target_codes)
    out = open('target.pkl', 'wb')
    pickle.dump(target_codes, out)
    return target_codes


def GetCodelist(df, x):
    print("Get code list")
    codes = []
    z = df.groupby(x).count()
    for y in z.index:
        codes.append(y)
    print str(codes)
    return codes


if __name__ == '__main__':
    main()

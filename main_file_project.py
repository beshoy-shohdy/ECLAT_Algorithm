import pandas as pd
from itertools import combinations
import numpy as np
import os

df = pd.read_csv('Horizontal_Format.xlsx - Sheet1.csv')

#unique
def unique1(df):
    df["items"] = df["items"].str.split(",")

    x = []

    for i in range(len(df)):
        for j in range(len(df["items"][i])):
            x.append(df["items"][i][j].strip())
    
    x = np.unique(x)

    return list(x)

#h to v
def htov(df, x):

    for i in x:
        df[i] = 0

    for index, items in df['items'].items():
        for item in items:
            df.loc[index, item] = 1

    df.drop(columns=['items'], inplace=True)

    df = df.set_index('TiD').T
    df = df.reset_index()

    return df

def make_b(df):
    b = {}

    for i in range(len(df)):
        item = df.iloc[i, 0]
        number = 0

        for v in df.iloc[i, 1:]:
            number = (number << 1) | int(v)

        b[item] = number

    return b

y = []

def make_pairs(x, ind=0, t=None):
    if t is None:
        t = []

    if ind >= len(x):
        y.append(t)
        return

    make_pairs(x, ind + 1, t)

    make_pairs(x, ind + 1, t + [x[ind]])


def get_support(bnum):
    
    return bin(bnum).count("1")

def rem_less_m_s(b,y):

    m_s_y = {}

    for i in y:
        andd = -1
        for item in i:
            if andd == -1:
                andd = b[item]
            else:
                andd = andd & b[item]

        s = get_support(andd)

        i = [str(item) for item in i]
        
        m_s_y[tuple(i)] = s
            
    return m_s_y

def get_levels(m_s_y):
    levels = {}
    for itemset, cnt in m_s_y.items():
        levels.setdefault(len(itemset), {})[itemset] = cnt

    cc = pd.DataFrame()

    for i in levels:
        for itemset, cnt in levels[i].items():
          cc = pd.concat([cc, pd.DataFrame({'Itemset': [list(itemset)], 'Support': [cnt]})], ignore_index=True)  

    return cc

def strong_rules(more_sup, n_trans, min_conf):

    rules = []

    for itemset, sup_ac in more_sup.items():
        for r in range(1, len(itemset)):
            for A in combinations(itemset, r):

                C = tuple(i for i in itemset if i not in A)

                sup_a = more_sup[tuple(sorted(A))]   
                sup_c = more_sup[tuple(sorted(C))]

                conf = sup_ac / sup_a
                lift = conf / (sup_c / n_trans)

                if conf >= min_conf:
                    rules.append({
                        'Rule': f"{list(A)} -> {list(C)}", 'Support': sup_ac / n_trans, 'Confidence': conf, 'Lift': lift,
                        'Dependency': 'positive' if lift > 1
                                      else 'negative' if lift < 1 else 'independent'
                    })

    return pd.DataFrame(rules).sort_values('Confidence', ascending=False)



sup = 3
conf = 0.8

df = pd.read_csv('Horizontal_Format.xlsx - Sheet1.csv')

x = unique1(df)

df = htov(df, x)

b = make_b(df)

make_pairs(x)

y = [x for x in y if x]

m_s_y = rem_less_m_s(b, y)

m_s_y_df = pd.DataFrame(
    [(list(itemset), support) for itemset, support in m_s_y.items()],
    columns=['Itemset', 'Support']
)

os.makedirs("output", exist_ok=True)

m_s_y_df.to_csv('output/all possible itemsets.csv', index=False)

more_sup = {}
for itemset, cnt in m_s_y.items():
    if cnt >= sup:
        more_sup[itemset] = cnt

levels = get_levels(more_sup)
levels.to_csv('output/frequent_itemsets.csv', index=False)

df_rules = strong_rules(more_sup, len(df.columns) - 1, conf)
df_rules.to_csv('output/strong_rules.csv', index=False)

print("-----------------------------All possible itemsets saved to 'all possible itemsets.csv' --------------------------------------------------------------")
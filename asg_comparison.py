import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from Functions import *


def load_adv():
    white = pd.read_csv('adv_data/dw_adv')
    white = extract_season(white, '2023-24')

    lillard = pd.read_csv('adv_data/dl_adv')
    lillard = extract_season(lillard, '2023-24')

    mitchell = pd.read_csv('adv_data/dm_adv')
    mitchell = extract_season(mitchell, '2023-24')

    hali = pd.read_csv('adv_data/th_adv')
    hali = extract_season(hali, '2023-24')

    brunson = pd.read_csv('adv_data/jb_adv')
    brunson = extract_season(brunson, '2023-24')

    maxey = pd.read_csv('adv_data/tm_adv')
    maxey = extract_season(maxey, '2023-24')

    trae = pd.read_csv('adv_data/ty_adv')
    trae = extract_season(trae, '2023-24')

    herro = pd.read_csv('adv_data/tho_adv')
    herro = extract_season(herro, '2023-24')

    dfs = [white, lillard, mitchell, hali, brunson, maxey, trae, herro]




    adv = pd.concat(dfs, axis=0, ignore_index=True)
    adv['Name'] = ['Derrick White', 'Damian Lillard', 'Donovan Mitchell', 'Tyrese Haliburton', 'Jalen Brunson', 'Tyrese Maxey', 'Trae Young', 'Tyler Herro']
    adv['O-EPM'] = [3.5, 4.3, 3.8, 8.3, 4.5, 4.8, 5.5, 2.2]
    adv['D-EPM'] = [1.9, 0.0, 0.4, -2.3, -0.9, -0.7, -0.6, 0.6]
    adv['EPM'] = [5.4, 4.3, 4.2, 5.9, 3.6, 4.1, 4.8, 2.8]

    new_column_name = {'WS/48': 'WS-48'}
    adv.rename(columns = new_column_name, inplace = True)
    return adv


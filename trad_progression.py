import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from Functions import *

dw_trad = pd.read_csv('https://raw.githubusercontent.com/Bhock37/AllStar/main/per_game')

dw_trad = filter_trades(dw_trad)
graph_progression(dw_trad, 'PTS')
graph_progression(dw_trad, 'AST')
graph_progression(dw_trad, 'TRB')
graph_progression(dw_trad, 'STL')

overlay_progression(dw_trad, ['PTS', 'AST', 'TRB', 'STL', 'BLK'])

print(dw_trad.head(10))

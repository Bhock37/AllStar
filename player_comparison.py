import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from Functions import *
from asg_comparison import load_adv

adv = load_adv()
print(adv.head(10))
print(adv.columns)

plot_comparison(adv, 'O-EPM')
plot_comparison(adv, 'D-EPM')
plot_comparison(adv, 'EPM')

plot_comparison(adv, 'OBPM')
plot_comparison(adv, 'DBPM')
plot_comparison(adv, 'BPM')

plot_comparison(adv, 'WS-48')

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def filter_trades(df):

    # Identify seasons where the player was not traded (only one team)
    single_team_seasons = df.groupby('Season')['Tm'].nunique() == 1
    single_team_mask = df['Season'].isin(single_team_seasons[single_team_seasons].index)

    # Identify 'total' rows
    total_mask = df['Tm'] == 'TOT'

    # Combine the masks to filter the DataFrame
    filtered_df = df[single_team_mask | total_mask].copy()

    return filtered_df

def graph_progression(df, stat):
    plt.figure()
    x = df['Season']
    y = df[stat]
    plt.plot(x, y, label = f'{stat}')
    plt.xlabel('Season')
    plt.ylabel(f'{stat}/Game')
    plt.legend()
    plt.savefig(f'{stat}_progression.png')

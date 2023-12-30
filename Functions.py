import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os


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

def overlay_progression(df, stats):
    plt.figure()
    x = df['Season']
    for stat in stats:
        y = df[stat]
        plt.plot(x, y, label = f'{stat}/Game')
    plt.xlabel('Season')
    plt.ylabel('Career Progression')
    plt.legend()
    plt.savefig('career_progression.png')

def extract_season(df, season):
    return df[df['Season'] == season]

def print_stat(df, stat):
    for i in range(len(df)):
        df = df.sort_values(by = stat, ascending = False)
        print(f"{df['Name'].iloc[i]}: {df[stat].iloc[i]} ({stat})")

def plot_comparison(df, stat):
    color_match = ['palegreen', 'forestgreen', 'maroon', 'gold', 'darkorange', 'blue', 'red', 'firebrick']
    names = df['Name']

    colors_dict = dict(zip(names, color_match))
    colors = [colors_dict[name] for name in names]


    plt.figure(figsize=(14, 12))

    plt.bar(df['Name'], df[stat], color=colors, width=0.6, label=names)

    plt.title(f'{stat} by Player', fontsize=16)
    plt.xlabel('Player', fontsize=14)
    plt.ylabel(f'{stat}', fontsize=14)

    project_directory = os.path.dirname(os.path.abspath(__file__))
    save_folder = 'bar_comparison'
    save_path = os.path.join(project_directory, save_folder, f'{stat}_bar_comparison.png')
    plt.savefig(save_path)

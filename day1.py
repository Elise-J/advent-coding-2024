import numpy as np
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('inputs/day1.csv', sep='   ', header=None, engine='python')

    # -- Part I
    # Sort values
    df[0] = df[0].sort_values(ignore_index=True)
    df[1] = df[1].sort_values(ignore_index=True)
    # Compute distance
    df["dist"] = abs(df[0] - df[1])
    # Sum distance
    print(f"Sum of the distances is: {df['dist'].sum()}")

    # -- Part II
    score = 0
    for val in df[0].drop_duplicates():
        nb_appearance_list1 = df[df[0] == val].shape[0]
        nb_appearance_list2 = df[df[1] == val].shape[0]
        score = score + nb_appearance_list1*nb_appearance_list2*val
    print(f"Similarity score : {score}")

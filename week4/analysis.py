#!/usr/bin/env python3
import pandas as pd
from pandas import DataFrame


def analysis(file, user_id):
    df = pd.read_json(file)
    df = df[df['user_id'] == user_id]['minutes']
    times = df.count()
    minutes = df.sum()
    return times, minutes


if __name__ == "__main__":
    analysis('user_study.json', 199071)

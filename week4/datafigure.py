#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

plt.ioff()


def data():
    df = pd.read_json('user_study.json')
    data = df.groupby('user_id').sum().head(50)
    print(data)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title = 'StudyData'
    ax.set_xlabel = 'UserID'
    ax.set_ylabel = 'Study Time'
    ax.plot(data.index, data.minutes)
    fig.show()
if __name__ == "__main__":
    data()

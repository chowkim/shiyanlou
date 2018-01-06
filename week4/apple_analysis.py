#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)
    volume = data.Volume
    volume.index = pd.to_datetime(data.Date)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(volume.index, volume)
    plt.show()
    second_quarter_volume = volume.resample('Q').sum().sort_values()[-2]
    return second_quarter_volume

quarter_volume()

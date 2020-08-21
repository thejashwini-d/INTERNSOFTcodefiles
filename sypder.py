# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:50:43 2020
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tasty = pd.read_csv('AAPL Historical Data.csv',usecols=[0,1,2,3,4])

tasty_avg = tasty[['Price','Open','High',]].mean(axis = 1)

red = np.arange(1,len(tasty)+1,1)

plt.plot(tasty_avg,red,'p',label = 'My Plot')

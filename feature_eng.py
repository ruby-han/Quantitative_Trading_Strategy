#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn import preprocessing

gain = lambda x: x if x > 0 else 0
loss = lambda x: abs(x) if x < 0 else 0

# Moving Average Convergence/Divergence        
def MACD(stock):
    short = stock.Close.ewm(span=12, adjust=False).mean()
    long = stock.Close.ewm(span=26, adjust=False).mean()
    macd = short-long
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal

# Bollinger Bands    
def bollinger_bands(stock, window=21):
    rolling_mean = stock.Close.rolling(window).mean()
    rolling_std = stock.Close.rolling(window).std()
    upper_band = rolling_mean + (rolling_std*2)
    lower_band = rolling_mean - (rolling_std*2)
    return upper_band, lower_band

# Relative Strength Index
def RSI(stock):    
    # Create a list, fill first 14 values with 'None'
    rsi_list = [None for i in range(14)]
    # Change as an input
    stock = (stock.Close - stock.Close.shift(1)).fillna(0)
    
    # Calculating first RSI
    avg_gain = sum([i for i in stock[1:15] if i > 0])/14
    avg_loss = sum([abs(i) for i in stock[1:15] if i < 0])/14
    rs = avg_gain / avg_loss
    rsi = 100 - ( 100 / ( 1 + rs ))
    rsi_list.append(rsi)
    
    # Calculating following RSI's
    for i in range(15, len(stock)):
        avg_gain = (avg_gain*13 + gain(stock[i]))/14
        avg_loss = (avg_loss*13 + loss(stock[i]))/14
        rs = avg_gain / avg_loss
        rsi = 100 - ( 100 / ( 1 + rs ))
        rsi_list.append(rsi)
    
    return rsi_list

def momentum(data, n_days):
    m = [None for i in range(n_days)]    
    for i in range(len(data) - n_days):
        end = i + n_days
        m.append(data[i] - n_days)
    return m


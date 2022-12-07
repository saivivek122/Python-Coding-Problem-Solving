import yfinance as yf
import pandas as pd
import datetime as dt
yf.pdr_override()
stock = input("enter stock")
year = 2019
month = 1
day = 1
start = dt.datetime(year,month,day)
now = dt.datetime.now()

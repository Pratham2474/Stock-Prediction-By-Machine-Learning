import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
import yfinance as yf


st.title("Stock price predictor App")

stock =st.text_input("Enter the stock ID", "AAPL")

from datetime import datetime
end =  datetime.now()
start= datetime(end.year-20, end.month,end.day)

aapl_data = yf.download(stock, start, end)

st.subheader("Stock Data")
st.write (aapl_data)


splitting_len = int(len(aapl_data)*0.7)
x_test = pd.DataFrame(aapl_data.Close[splitting_len:])

def plot_graph(figsize, values, full_data):
    fig = plt.figsize(figsize=figsize)
    plt.plot(values, 'Orange')
    plt.plot(full_data.close, 'b')
    return fig

import streamlit as st

import plotly.express as px
import matplotlib.pyplot as plt
import yfinance as yf
 
#Selectbox 
options = st.multiselect('Escoge la empresa de la que quieras ver sus acciones', ('Google', 'Tesla', 'Microsoft', 'Apple'))
#Creamos una lista con los tickers a descargar
#lista_precios = ['TSLA', 'GOOG', 'MSFT', 'AAPL']
#Descargamos todos los tickers de la lista y sólo los datos que necesitamos
data = yf.download(options, start="2012-01-01")['Adj Close']

 

print(type (options))
print(type(data))
# data = yf.download(options, start="2012-01-01")['Adj Close']

st.line_chart(data)
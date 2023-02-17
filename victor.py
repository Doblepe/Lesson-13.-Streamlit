import streamlit as st
import yfinance as yf
# #Selectbox 
# dict = {"Google": 'GOOGL',
#         "Tesla": "TSL",
#         "Microsoft": "MSFT",
#         "Apple": "AAPL"}

options = st.multiselect('Escoge la empresa de la que quieras ver sus acciones', ('GOOGL', 'TSL', 'MSFT', 'AAPL'))

#companies = ('GOOGL', 'TSL', 'MSFT', 'AAPL')


def show_results(options): 
    for opt in options:
        st.write('Las empresa seleccionada es', opt)
        data = yf.download(opt, start="2012-01-01")['Adj Close']
        st.line_chart(data)



show_results(options)



#data = yf.download(companies, start="2012-01-01")['Adj Close']

 



# data = yf.download(options, start="2012-01-01")['Adj Close']

#st.line_chart(data)

import streamlit as st
import yfinance as yf
# #Selectbox 
#TODO: FIX with de dict to set the full companies name
# dict = {"Google": 'GOOGL',
#         "Tesla": "TSL",
#         "Microsoft": "MSFT",
#         "Apple": "AAPL"}
date = st.date_input
options = st.multiselect('Escoge la empresa de la que quieras ver sus acciones', ('GOOGL', 'TSL', 'MSFT', 'AAPL','AMZN'))

#companies = ('GOOGL', 'TSL', 'MSFT', 'AAPL')
def show_results(options):
    #transformo las options a list para poder descargarla
    options = list(options)
    if options.__len__() == 0:
        st.write('Todavía no has seleccionado ninguna empresa')
    else:
        data = yf.download(options, start="2012-01-01")['Adj Close']
        st.line_chart(data)
    


#def show_several_boxes(options):
    # for opt in options:
    #     st.write('Las empresa seleccionada es', opt)
    #     data = yf.download(opt, start="2012-01-01")['Adj Close']
    #     print(data)
         


show_results(options)



#data = yf.download(companies, start="2012-01-01")['Adj Close']

 



# data = yf.download(options, start="2012-01-01")['Adj Close']

#st.line_chart(data)

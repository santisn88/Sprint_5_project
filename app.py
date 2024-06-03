import pandas as pd
import streamlit as st
import plotly.express as px

# Leer los datos del documento csv con la ruta especificada
car_data_df = pd.read_csv("vehicles_us.csv")

# Imprimir una muestra de la lectura de los datos
st.write('Esta es mi primera aplicacion en Streamlit')
st.write('Esta contiene informacion de vehiculos de venta en Estados Unidos')
st.write('Muestra de los datos cargados')

st.write(car_data_df.head()) 

def histogram_graph():
    fig = px.histogram(car_data_df, x = 'odometer',
                       labels = {
                           'odometer' : 'Odometro',
                       },
                       title = 'Odometro de los vehiculos'
    )                                                      
    st.plotly_chart(fig, use_container_width=True)

def scatter_graph():
    fig = px.scatter(car_data_df, x = 'model_year', y = 'price',
                       labels = {
                           'model_year' : 'Ano de los modelos',
                           'price' : 'Precios de los modelos'
                       },
                       title = 'Precio de los vehiculos en relacion a los anos de modelo'
    )                                                      
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para el histograma y scatter
st.write("Este histograma contiene la infomracion del odometro de todos los carros de venta")
histogram_button = st.button('Construir histograma')
st.write("Este grafico de dispersion contiene la infomracion del precio y del ano de modelo")
scatter_button = st.button('Construir grafico dispersion')

# Al hacer clic en el botón los graficos se activan
if histogram_button:
    histogram_graph()

if scatter_button:
    scatter_graph()
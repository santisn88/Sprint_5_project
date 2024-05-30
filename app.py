import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv("G:\My Drive\Personal\Git Hub\Sprint_5_project\Vehicles_us.csv")
print(car_data[car_data['is_4wd'].isna()])
'''
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("G:\My Drive\Personal\Git Hub\Sprint_5_project\Vehicles_us.csv") # leer los datos
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
'''
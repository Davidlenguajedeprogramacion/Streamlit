import streamlit as st
import pandas as pd
from io import StringIO

def process_sales(file_content):
    totalVentas = 0.0
    numDias = 0
    maxDate, minDate = "", ""
    maxVenta = -float('inf')
    minVenta = float('inf')

    lines = file_content.splitlines()
    for line in lines:
        date, venta = line.strip().split(',')
        venta = float(venta)

        totalVentas += venta
        numDias += 1

        if venta > maxVenta:
            maxVenta = venta
            maxDate = date
        if venta < minVenta:
            minVenta = venta
            minDate = date

    promedioVentas = totalVentas / numDias if numDias > 0 else 0

    return totalVentas, promedioVentas, maxDate, maxVenta, minDate, minVenta

def main():
    st.title("Registro de Ventas Diarias")

    uploaded_file = st.file_uploader("Sube tu archivo de ventas diarias", type=["txt"])
    
    if uploaded_file is not None:
        # Leer el archivo como cadena de texto
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        file_content = stringio.read()

        totalVentas, promedioVentas, maxDate, maxVenta, minDate, minVenta = process_sales(file_content)
        
        st.write("### Resultados")
        st.write(f"Venta total: {totalVentas}")
        st.write(f"Promedio de ventas: {promedioVentas:.2f}")
        st.write(f"Día de mayor venta: {maxDate}, {maxVenta}")
        st.write(f"Día de menor venta: {minDate}, {minVenta}")
        
        # Crear el contenido del archivo de salida
        output_content = (
            f"Venta total: {totalVentas}\n"
            f"Promedio de ventas: {promedioVentas:.2f}\n"
            f"Día de mayor venta: {maxDate}, {maxVenta}\n"
            f"Día de menor venta: {minDate}, {minVenta}\n"
        )
        
        # Permitir al usuario descargar los resultados
        st.download_button(
            label="Descargar resultados",
            data=output_content.encode('utf-8'),
            file_name='resumen_ventas.txt',
            mime='text/plain',
        )

if __name__ == "__main__":
    main()

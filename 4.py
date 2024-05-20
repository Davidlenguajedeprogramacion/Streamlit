import streamlit as st
import pandas as pd
from io import StringIO

def process_temperatures(file_content):
    maxDate, minDate = "", ""
    maxTemp = -float('inf')
    minTemp = float('inf')

    lines = file_content.splitlines()
    for line in lines:
        date, temp = line.strip().split(',')
        temp = float(temp)

        if temp > maxTemp:
            maxTemp = temp
            maxDate = date
        if temp < minTemp:
            minTemp = temp
            minDate = date

    return maxDate, maxTemp, minDate, minTemp

def main():
    st.title("Registro de Temperaturas Diarias")

    uploaded_file = st.file_uploader("Sube tu archivo de temperaturas", type=["txt"])
    
    if uploaded_file is not None:
        # To read file as string:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        file_content = stringio.read()

        maxDate, maxTemp, minDate, minTemp = process_temperatures(file_content)
        
        st.write("### Resultados")
        st.write(f"Día de temperatura máxima: {maxDate}, {maxTemp}")
        st.write(f"Día de temperatura mínima: {minDate}, {minTemp}")
        
        # Create the output content
        output_content = (
            f"Día de temperatura máxima: {maxDate}, {maxTemp}\n"
            f"Día de temperatura mínima: {minDate}, {minTemp}\n"
        )
        
        # Allow user to download the results
        st.download_button(
            label="Descargar resultados",
            data=output_content.encode('utf-8'),
            file_name='extremas.txt',
            mime='text/plain',
        )

if __name__ == "__main__":
    main()

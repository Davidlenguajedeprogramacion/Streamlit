import streamlit as st
import pandas as pd
from io import StringIO

def process_log_file(file_content):
    errorCount = {}

    lines = file_content.splitlines()
    for line in lines:
        errorType = line.split(':')[0]
        if errorType in errorCount:
            errorCount[errorType] += 1
        else:
            errorCount[errorType] = 1

    return errorCount

def main():
    st.title("Resumen de Errores en Archivo de Log")
    
    uploaded_file = st.file_uploader("Sube tu archivo de log de errores", type=["txt"])
    
    if uploaded_file is not None:
        # To read file as string:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        file_content = stringio.read()

        errorCount = process_log_file(file_content)
        
        st.write("### Resumen de Errores")
        df = pd.DataFrame(list(errorCount.items()), columns=['Tipo de Error', 'Cantidad'])
        st.dataframe(df)
        
        # Create a downloadable CSV file
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Descargar resumen como CSV",
            data=csv,
            file_name='resumen_errores.csv',
            mime='text/csv',
        )

if __name__ == "__main__":
    main()

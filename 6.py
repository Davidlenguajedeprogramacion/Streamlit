import streamlit as st
from io import StringIO

def process_hours(file_content):
    horasPorEmpleado = {}

    lines = file_content.splitlines()
    for line in lines:
        nombre, horas = line.strip().split(',')
        horas = int(horas)

        if nombre not in horasPorEmpleado:
            horasPorEmpleado[nombre] = horas
        else:
            horasPorEmpleado[nombre] += horas

    return horasPorEmpleado

def main():
    st.title("Registro de Horas Trabajadas")

    uploaded_file = st.file_uploader("Sube tu archivo de registro de horas", type=["txt"])
    
    if uploaded_file is not None:
        # Leer el archivo como cadena de texto
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        file_content = stringio.read()

        horasPorEmpleado = process_hours(file_content)
        
        st.write("### Resultados")
        for nombre, horas in horasPorEmpleado.items():
            st.write(f"{nombre}, Horas Totales: {horas}")
        
        # Crear el contenido del archivo de salida
        output_content = ""
        for nombre, horas in horasPorEmpleado.items():
            output_content += f"{nombre}, Horas Totales: {horas}\n"
        
        # Permitir al usuario descargar los resultados
        st.download_button(
            label="Descargar resultados",
            data=output_content.encode('utf-8'),
            file_name='informe_horas_totales.txt',
            mime='text/plain',
        )

if __name__ == "__main__":
    main()

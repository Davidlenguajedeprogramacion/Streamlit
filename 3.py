import streamlit as st

# Función para convertir precios de dólares a otra moneda
def convertir_precios(lines, tasa_conversion):
    resultados = []
    for line in lines:
        nombre, precio_dolares = line.strip().split(',')
        precio_dolares = float(precio_dolares)
        precio_convertido = precio_dolares * tasa_conversion
        resultados.append(f"{nombre}, Precio Convertido: {precio_convertido:.2f}")
    return resultados

def main():
    st.title("Conversor de Precios de Dólares a Soles")

    uploaded_file = st.file_uploader("Sube tu archivo de precios en dólares", type="txt")
    tasa_conversion = 3.85  # Tasa de conversión de dólares a soles

    if uploaded_file is not None:
        lines = uploaded_file.readlines()
        resultados = convertir_precios([line.decode("utf-8") for line in lines], tasa_conversion)

        if resultados:
            st.write("Resultados:")
            for resultado in resultados:
                st.write(resultado)

            if st.button("Descargar resultado"):
                result_text = "\n".join(resultados)
                st.download_button(
                    label="Descargar precios_convertidos.txt",
                    data=result_text,
                    file_name="precios_convertidos.txt",
                    mime="text/plain",
                )
        else:
            st.write("No se encontraron precios para convertir.")

if __name__ == "__main__":
    main()

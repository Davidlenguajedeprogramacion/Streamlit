import streamlit as st

def calcular_promedios(lines):
    resultados = []
    for line in lines:
        parts = line.strip().split(',')
        nombre = parts[0]
        sumaNotas = 0
        numNotas = 0
        
        for part in parts[1:]:
            materia, nota = part.split(':')
            nota = float(nota)
            sumaNotas += nota
            numNotas += 1

        promedio = sumaNotas / numNotas if numNotas > 0 else 0
        resultados.append(f"{nombre}, Promedio: {promedio:.2f}")
    return resultados

def main():
    st.title("Calculadora de Promedios de Notas")

    uploaded_file = st.file_uploader("Sube tu archivo de notas", type="txt")

    if uploaded_file is not None:
        lines = uploaded_file.readlines()
        resultados = calcular_promedios([line.decode("utf-8") for line in lines])

        if resultados:
            st.write("Resultados:")
            for resultado in resultados:
                st.write(resultado)

            if st.button("Descargar resultado"):
                result_text = "\n".join(resultados)
                st.download_button(
                    label="Descargar promedios.txt",
                    data=result_text,
                    file_name="promedios.txt",
                    mime="text/plain",
                )
        else:
            st.write("No se encontraron notas para calcular promedios.")

if __name__ == "__main__":
    main()

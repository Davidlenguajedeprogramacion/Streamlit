import streamlit as st

def main():
    st.title("Filtrado de Correos Electrónicos")

    uploaded_file = st.file_uploader("Sube tu archivo de datos personales", type="txt")
    
    if uploaded_file is not None:
        lines = uploaded_file.readlines()
        emails_filtrados = []

        for line in lines:
            line = line.decode("utf-8").strip()
            nombre, rest = line.split(',', 1)
            edad, email = rest.split(',', 1)
            edad = int(edad)
            
            if edad > 18:
                emails_filtrados.append(email)

        if emails_filtrados:
            st.write("Correos electrónicos filtrados:")
            for email in emails_filtrados:
                st.write(email)
            
            if st.button("Descargar resultado"):
                result = "\n".join(emails_filtrados)
                st.download_button(
                    label="Descargar emails_filtrados.txt",
                    data=result,
                    file_name="emails_filtrados.txt",
                    mime="text/plain",
                )
        else:
            st.write("No hay correos electrónicos de personas mayores de 18 años.")

if __name__ == "__main__":
    main()

# Coluns
# text_input
# button
# int
# if e else

import streamlit as st 

cols =st.columns(4)


numero1=st.text_input ('Digite um numero')
numero2=st.text_input ('Digite o segundo numero')

with cols [0]:
    st.write('coluna 1')

    if st.button ('soma'):
        resultado=int (numero1)+ int (numero2)
        st.text (f" o resultado é {resultado}")

with cols [1]:
    if st.button ('subtrair'):
      resultado=int (numero1)-int (numero2)
      st.text (f" o resultado é {resultado}")

with cols[2]:
    if st.button ('multiplicar'):
        resultado=int (numero1)*int (numero2)
        st.text (f' o resultado é {resultado}')

with cols[3]:
    if st.button ('divisão'):
        resultado=int (numero1) / int (numero2)
        st.text(f' o resultado é {resultado}')


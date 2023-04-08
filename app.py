#library
import streamlit as st

# write 
st.title('Software perkalian')
st.subheader('Ini adalah aplikasi untuk mengalikan bilangan')

# input bilangan pertama
number1 = st.number_input('Masukkan bilangan pertama')
st.write(f'Bilangan pertama adalah {number1}')

number2 = st.number_input('Masukkan bilangan kedua')
st.write(f'Bilangan kedua adalah {number2}')

#hasil kali
tombol = st.button('hitung perkalian')

if tombol:
    hasil = number1*number2
    st.write(f'Hasil kali antara {number1} dan {number2} adalah {hasil}')
    st.balloons()
else:
    st.write('Silakan pencet tombol hitung!')
    
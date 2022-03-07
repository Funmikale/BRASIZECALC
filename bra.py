import streamlit as st 
from PIL import Image 

st.write(""" 
# BRA SIZE CALCULATOR!
""")
image=Image.open('MGGN.jpg')
st.image(image)

st.sidebar.write(""" # KNOW YOUR BRASTORY!
Throughout the fight for women's right as early as the women's march, bras have held a poetic significance,
                 they have been burned,hunged and swung in protest. 
                 Those actions resulted in the world we live today where women have CHOICES, the CHOICES that afford us the
                 opportunity to decide who/what we want to be or simply to wear a bra or not, 
                 in the light of this it is important that we spill our quota and leave an impact
                 that will sustain our world tommorow.
                 
                 HAPPY INTERNATIONAL WOMEN'S DAY
                 FEYISAYO DAISI
                 MGGN AMBASSADOR 2021""")

Band_size=st.number_input('What is your Band size?')

Bust_size=st.number_input('What is your bust size?')

st.write(""" # HOW TO USE
1.Measure Bust Size: Area around your bust 
2.Measure Band Size: Area under your rib cage under your bust 
3.Input the measurements in as required
4.Press enter to apply."""

Band = (Band_size+3)
if Band%2!=0:
     Band=int((Band + 1))
else:
    Band=int(Band)
Bust =(Bust_size-Band)
if Bust== 0:
    st.write('Your Bra size is',Band,'AA')
elif Bust == 1:
    st.write('Your Bra size is ',Band,'A')
elif Bust== 2:
    st.write('Your Bra size is ',Band,'B')
elif Bust == 3:
    st.write('Your Bra size is ',Band,'C')
elif Bust == 4:
    st.write('Your Bra size is ',Band,'D')
elif Bust == 5:
    st.write('Your Bra size is ',Band,'DD/E')
else:
    st.write('Your Bra size is ',Band,'DDD/F')

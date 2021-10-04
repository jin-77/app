import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title('Streamlit')
#st.write('DataFrame')
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range (100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
'Done!!'


left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字表示')
if button:
    right_column.write('ここは右カラムです')
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容3')

#text = st.text_input('あなたの趣味をお教えてください。')
#condition = st.slider('あなたの調子は？',0 ,100, 50)
#'あなたの趣味', text
#'コンディション：', condition





#if st.checkbox('Show Image'):
 #   img = Image.open('sample.jpg')
 #   st.image(img, caption='Jin', use_column_width= True)
 



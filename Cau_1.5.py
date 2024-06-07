import streamlit as st 
import numpy as np
import pandas as pd
st.title("My first ...")
st.header("Header ...")
st.text('Đây là text')
st.markdown('Markdown đây **anh em ơi**')
st.write('Còn dưới đây ...')
st.latex(r'''a+b=3''')
st.write(12345)
st.code('''def hello:
    print("Hello world")''', language='python')
st.text("Hiển thị luôn cả chart")
data = np.random.randn()
df = pd.DataFrame(data, columns=['a', 'b', 'c'])
st.line_chart(df)
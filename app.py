import streamlit as st
import pandas as pd
import numpy as np

st.write('Sample App')
st.title('Sample App')
st.code("""
import numpy as np
import pandas as pd
a = 123
pd.DataFrame()
""")

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [-1, -2, -3, -4],

})

st.dataframe(df.style.highlight_max(axis=0))

st.json({
    'data': {
        'name': 'abc',
        'age': 123
    }
})

df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)


st.line_chart(df)
st.bar_chart(df)


if st.button('Click Me!!!!!!!!!!!!'):
    st.write('Clicked')

if st.checkbox('Click Me!!!!!!!!!!!!'):
    st.write('Clicked')


st.file_uploader("ファイルアップロード", type='jpg')


options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)


color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)


number = st.sidebar.slider('Pick a Num', 0, 100, 40)
st.sidebar.write(f'number: {number}')
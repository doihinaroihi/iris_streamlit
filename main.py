# 必要なライブラリをインポート
import streamlit as st
import numpy as np
import pandas as pd

# タイトルとテキストを記入
st.title('Streamlit 基礎')
st.write('Hello World!')

# データフレームの準備
df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})

# 引数を使用した動的テーブル
st.dataframe(df.style.highlight_max(axis = 0) , width = 100 , height = 150)
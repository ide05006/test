3

import streamlit as st

st.write("Hello, *World!* :sunglasses:")
st.set_page_config()

st.write("파이썬")
"# 파이썬"
"## 파이썬"
"### 파이썬"
"#### 파이썬"
"##### 파이썬"
"###### *파이썬*의 :red[세계에] 오신"

st.html("<h1>파이썬</h1>")
st.html("<h2>파이썬</h2>")

import streamlit as st

st.sidebar.write("사이드바")

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

import streamlit as st
import numpy as np
import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig)

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 07:34:38 2021

@author: evan
"""

import streamlit as st
import pandas as pd
st.title('SF Trees')
st.write('This app analyses trees in San Francisco using'
         ' a dataset kindly provided by SF DPW')
trees_df = pd.read_csv('C:/Users/evan/Documents/Streamlit_apps/trees_app/trees.csv')
st.write(trees_df.head())

# group our dataset by width, count the unique trees of each width, and then make a line, bar, and area chart of each
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)

# sample 1,000 random rows from our DataFrame, remove null values, and try out st.map()
trees_df = pd.read_csv('C:/Users/evan/Documents/Streamlit_apps/trees_app/trees.csv')
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n = 1000)
st.map(trees_df)

# histogram of the height of the trees in SF with plotly
import plotly.express as px
st.subheader('Plotly Chart')
trees_df = pd.read_csv('C:/Users/evan/Documents/Streamlit_apps/trees_app/trees.csv')
fig = px.histogram(trees_df['dbh'])
st.plotly_chart(fig)


# he following code creates a new column called age, which is the difference in days between 
# the tree planting date and today, and then graphs the histogram of the age using both Seaborn and Matplotlib
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
trees_df = pd.read_csv('C:/Users/evan/Documents/Streamlit_apps/trees_app/trees.csv')
trees_df['age'] = (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])).dt.days
st.subheader('Seaborn Chart') 
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.distplot(trees_df['age'])
plt.xlabel('Age (Days)')
st.pyplot(fig_sb)
st.subheader('Matploblib Chart')
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df['age'])
plt.xlabel('Age (Days)')
st.pyplot(fig_mpl)

# Bokeh
from bokeh.plotting import figure
st.subheader('Bokeh Chart')
trees_df = pd.read_csv('C:/Users/evan/Documents/Streamlit_apps/trees_app/trees.csv')
scatterplot = figure(title = 'Bokeh Scatterplot')
scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
scatterplot.yaxis.axis_label = "site_order"
scatterplot.xaxis.axis_label = "dbh"
st.bokeh_chart(scatterplot)

# Altair
import altair as alt
trees_df = pd.read_csv('C:/Users/evan/Documents/Streamlit_apps/trees_app/trees.csv')
df_caretaker = trees_df.groupby(['caretaker']).count()['tree_id'].reset_index()
df_caretaker.columns = ['caretaker', 'tree_count']
fig = alt.Chart(df_caretaker).mark_bar().encode(x = 'caretaker', y = 'tree_count')
st.altair_chart(fig)

# PyDeck for geographic mapping costs $





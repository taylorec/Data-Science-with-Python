# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:48:12 2021

@author: evan
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title("Palmer's Penguins")
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')
 
penguin_file = st.file_uploader('Select Your Local Penguins CSV (default provided)')
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    penguins_df = pd.read_csv('C:/Users/evan/Documents/Streamlit_apps/penguin_app/penguins.csv')
    
selected_x_var = st.selectbox('What do want the x variable to be?', ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?', ['culmen_depth_mm', 'culmen_length_mm', 'flipper_length_mm', 'body_mass_g'])
 
fig, ax = plt.subplots()
ax = sns.scatterplot(x = penguins_df[selected_x_var],
     y = penguins_df[selected_y_var], hue = penguins_df['species'])
plt.xlabel(selected_x_var) 
plt.ylabel(selected_y_var)
plt.title("Scatterplot of Palmer's Penguins")
st.pyplot(fig)
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 19:55:13 2021

@author: evan
"""





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title("Palmer's Penguins")
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!') 
selected_species = st.selectbox('What species would you like to visualize?', ['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox('What do want the x variable to be?', ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?', ['culmen_depth_mm', 'culmen_length_mm', 'flipper_length_mm', 'body_mass_g'])
selected_gender = st.selectbox('What gender do you want to filter for?', ['all penguins', 'male penguins', 'female'])

penguin_file = st.file_uploader('Select Your Local Penguins CSV (default provided)')
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    penguins_df = pd.read_csv('C:/Users/evan/Documents/Streamlit_apps/penguin_app/penguins.csv')

if selected_gender == 'male penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == 'female penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
   pass
                              
penguins_df = pd.read_csv('C:/Users/evan/Documents/Streamlit_apps/penguin_app/penguins.csv')
penguins_df = penguins_df.drop('Unnamed: 0', axis=1)

sns.set_style('darkgrid')
fig, ax = plt.subplots()
ax = sns.scatterplot(data = penguins_df, x = selected_x_var, y = selected_y_var, hue = 'species', style = 'species')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title('Scatterplot of {} Penguins'.format(selected_species))
st.pyplot(fig)
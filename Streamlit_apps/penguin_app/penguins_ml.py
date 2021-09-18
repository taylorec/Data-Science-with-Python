# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 08:51:37 2021

@author: evan
"""

import pandas as pd
penguin_df = pd.read_csv('C:/Users/evan/Documents/Streamlit_apps/penguin_app/penguins.csv')
penguin_df = penguin_df.drop('Unnamed: 0', axis=1)
penguin_df = penguin_df.drop(penguin_df.index[164])
penguin_df.dropna(inplace=True)
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
output = penguin_df['species']
features = penguin_df[['island', 'culmen_length_mm', 'culmen_depth_mm',
                       'flipper_length_mm', 'body_mass_g', 'sex']]
features = pd.get_dummies(features)
output, uniques = pd.factorize(output)
x_train, x_test, y_train, y_test = train_test_split(features, 
                                                    output, test_size=.8)
rfc = RandomForestClassifier(random_state=15)
rfc.fit(x_train, y_train)
y_pred = rfc.predict(x_test)
score = accuracy_score(y_pred, y_test)
print('Our accuracy score for this model is {}'.format(score))

rf_pickle = open('random_forest_penguin.pickle', 'wb')
pickle.dump(rfc, rf_pickle)
rf_pickle.close()
output_pickle = open('output_penguin.pickle', 'wb')
pickle.dump(uniques, output_pickle)
output_pickle.close() 
import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots()
ax = sns.barplot(rfc.feature_importances_, features.columns)
plt.title('Which features are the most important for species prediction?')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.tight_layout()
fig.savefig('feature_importance.png')

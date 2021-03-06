# -*- coding: utf-8 -*-
"""PharmaceuticalsDiscovery .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dwcRgywrz3kqCfptNs3jEpZ0Ahw9yE2z
"""

import pandas as pd

url_data = "https://github.com/rlatorraca/PharmaceuticalsDiscovery/blob/master/data/dados_experimentos.zip?raw=true"

# Create a DATA FRAME
data = pd.read_csv(url_data, compression = 'zip')

"""Cada linha é um ***cultura de celula*** que foi submetido a inclusão de drogas para que possam ser estudadas as suas respostas ao experimento.

- id = identificador único
- tratamento = [com droga | com controle]


"""

# Show first 5 rows on Data Frame
data.head()

# Last 5 rows on Data Frame
data.tail()

# Number of row and colummns
data.shape

# Just plot the Column = tratamento (Series)
data['tratamento']

# Return the uniques values of the Column
data['tratamento'].unique()

# Time of exposure to the drug before analyzing the responses to that exposure.
data['tempo'].unique()

# 2 differents quantity of drugs
data['dose'].unique()

# Total of drugs in this Data Frame
# "Encrypted / modified" data to make analysis less biased
data['droga'].unique()

# g = gene
data['g-0'].unique()

# Frequency in 'Tratamento'
data['tratamento'].value_counts()

# Calculus of the proportion of experiments in 'TRATAMENTO' with "Drogas" and "Controle": 
trat_values = data['tratamento'].value_counts()
proportion_tratamento = trat_values[0] / trat_values[1]
print(proportion_tratamento)

# OR Normalize in 'TRATAMENTO'
data['tratamento'].value_counts(normalize = 'true')

data['tratamento'].value_counts(normalize = 'true').plot.bar()

# Frequency in 'Doses'
data['dose'].value_counts()

# Calculus of the proportion of experiments in 'DOSE'with "D1" and "D2": 
dose_values = data['dose'].value_counts()
proportion_dose = dose_values[0] / dose_values[1]
print(proportion_dose)

# OR Normalize in 'DOSE'
data['dose'].value_counts(normalize = 'true')

data['dose'].value_counts(normalize = 'true').plot.bar()

# Just printing g-0 > 0
data[data['g-0'] > 0]

# Put on atribute g-0 > ZERO
g0_upper_zero = data[data['g-0'] > 0]

# Print the new DF g-0 > ZERO
g0_upper_zero.head()

data.rename(columns = {'g-0': 'Year', 'value': 'Income'}, inplace = False)

# Change name of column 'droga'to 'composto'
map = {'droga': 'composto'}
data.rename(columns=map, inplace=True)

data.head()

# importing SEABORN
import seaborn as sns

# Ploting all values of column composto
# Bad visualization
sns.countplot(x='composto', data=data)

# Ploting just the 5 bigger compostos in numbers
compostos = data['composto'].value_counts()[:10]

compostos.index

# Ploting just the 5 bigger index of compostos
code_compostos = data['composto'].value_counts().index[:10]

code_compostos

# getting just the row of 5 bigger in numbers
data.query('composto in @code_compostos')

# Set up and importing Matplotlib
import matplotlib.pyplot as plt
sns.set()

# Ploting 10 bigger compostos
data_compostos = data.query('composto in @code_compostos')
plt.figure(figsize=(20,10))
ax = sns.countplot(x='composto', data=data_compostos)
ax.set_title('Top 10 de Compostos')
plt.show()

# how many g-0 do we have ?
len(data['g-0'].unique())

# Min value in g-0 field
data['g-0'].min()

# Max value in g-0 field
data['g-0'].max()

# Histogram for g-10 and bins = 50
data['g-0'].hist(bins = 50)

# Histogram for g-10 and bins = 100
data['g-0'].hist(bins = 100)

# Histogram for g-10 and bins = 150
data['g-0'].hist(bins = 150)

# Histogram for g-222 and bins = 150
data['g-222'].hist(bins = 150)

# Generan Information about the DataFrame
data.describe()

# Just g-0 and g-1 generan information
data[{'g-0', 'g-1'}].describe()

# Show general data for g-0 to g-771
# : => slices getting all rows
# 'g-0' : => slices getting all rows from 0 to LAST element
data.loc[:, 'g-0':].describe()

# MEAN in Histogram
# Needs to do a Transpose Matrix
data.loc[:, 'g-0':].describe().T

# MEAN Histogram plot
data.loc[:, 'g-0':].describe().T['mean'].hist(bins = 50)

# MIN Histogram plot
data.loc[:, 'g-0':].describe().T['min'].hist(bins = 50)

# MAX Histogram plot
data.loc[:, 'g-0':].describe().T['max'].hist(bins = 50)

# Show general data for c-0 to c-99
# : => slices getting all rows
# 'c-0' : => slices getting all rows from 0 to LAST element
data.loc[:, 'c-0':].describe()

# MEAN Histogram plot
data.loc[:, 'c-0':].describe().T['mean'].hist(bins = 50)

# MIN Histogram plot
data.loc[:, 'g-0':].describe().T['min'].hist(bins = 50)

# MAX Histogram plot
data.loc[:, 'g-0':].describe().T['max'].hist(bins = 50)

# Box Plot Graphic example
sns.boxplot(x='g-0', data=data)

#BoxPlot using 'tratamento' in Y axis
sns.boxplot(x='g-0', y='tratamento', data=data)

#BoxPlot using 'tratamento in x axis (Rotation)
plt.figure(figsize=(12,8))
sns.boxplot(y='g-0', x='tratamento', data=data)

# Correlation between DOSES and TEMPO
pd.crosstab(data['dose'], data['tratamento'])

# Correlation between (DOSES and TEMPO) and Tempo
pd.crosstab([data['dose'], data['tempo']], data['tratamento'])

# Correlation between (DOSES and TEMPO) and Tempo
# Normalize to all matrix
pd.crosstab([data['dose'], data['tempo']], data['tratamento'], normalize=True)

# Correlation between (DOSES and TEMPO) and Tempo
# Normalize by row
pd.crosstab([data['dose'], data['tempo']], data['tratamento'], normalize='index')

# Mean of 'g-0'gene with CONTROLE or with DROGA
pd.crosstab([data['dose'], data['tempo']], data['tratamento'], values=data[ 'g-0'], aggfunc='mean')

# Cartesian Plan
# loooking for some pattern
sns.scatterplot(x='g-0', y='g-3', data=data)

data[['g-0', 'g-3']]

sns.scatterplot(x='g-0', y='g-8', data=data)

# Adding trend line
sns.lmplot(x='g-0', y='g-8', data=data, line_kws={'color': 'red'})

# Adding trend line to 'g-0 x g-8' when added 'droga' or not
sns.lmplot(x='g-0', y='g-8', data=data, line_kws={'color': 'red'}, col='tratamento')

# Adding trend line to 'g-0 x g-8' when added 'droga' or not, by tempo
sns.lmplot(x='g-0', y='g-8', data=data, line_kws={'color': 'red'}, col='tratamento', row='tempo')

# Correlation to all genes
data.loc[:, 'g-0': ].corr()

# Compute the correlation matrix
import numpy as np
corr_genes = data.loc[:, 'g-0':'g-50'].corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr_genes, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(15, 15))
# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)
# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr_genes, mask=mask, cmap=cmap, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})

# Compute the correlation matrix
corr_cels = data.loc[:, 'c-0':'c-50'].corr()

# Generate a mask for the upper triangle
mask_cels = np.triu(np.ones_like(corr_cels, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(15, 15))
# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)
# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr_cels, mask=mask, cmap=cmap, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})

###
### DATA MERGE and RESULT ANALYSIS
###
url_data = "https://github.com/rlatorraca/PharmaceuticalsDiscovery/blob/master/data/dados_resultados.csv?raw=true"

data_results = pd.read_csv(url_data)

data_results.head()

data_results['acat_inhibitor'].unique()

# Just SUM by columns numeric values, excluding ID
#  data_results.drop('id', axis = 1).sum().sort_values(ascending=False)
counter_mecanismOfAction_col = data_results.select_dtypes('int64').sum().sort_values(ascending=False)
counter_mecanismOfAction_col

data_results.info()

# Just SUM by row numeric values, excluding ID
#  data_results.drop('id', axis = 1).sum().sort_values(ascending=False)
counter_mecanismOfAction_rows = data_results.select_dtypes('int64').sum(axis=1)
counter_mecanismOfAction_rows.sort_values(ascending=False)

counter_mecanismOfAction_rows

# total Mechanism of Action = 'n_moa'
data_results['n_moa'] = counter_mecanismOfAction_rows 
data_results.head()

data_results.head()

# active or not Actio mechanism = active_moa
data_results['active_moa'] = (data_results['n_moa'] != 0)
data_results.head()

# MERGING the 2 DB
data_merged = pd.merge(data, data_results[['id','n_moa', 'active_moa']], on='id')
data_merged

data_merged.query('tratamento == "com_controle"')['active_moa'].value_counts()

data_merged.query('tratamento == "com_droga"')['active_moa'].value_counts()

principal_composts = data_merged['composto'].value_counts().index[:11]
principal_composts

# Distribution to 'g-0'
plt.figure(figsize=(25,15))
sns.boxplot(data=data_merged, y='g-0', x='composto')

plt.figure(figsize=(20,25))
sns.boxplot(data=data_merged.query('composto in @principal_composts'), y='g-0', x='composto',hue='active_moa')

plt.figure(figsize=(30,25))
sns.catplot(data=data_merged.query('composto in @principal_composts'), y='g-0', x='composto',hue='active_moa', col='dose', kind="box",  height=15)

plt.figure(figsize=(30,25))
sns.catplot(data=data_merged.query('composto in @principal_composts'), y='g-0', x='composto',hue='active_moa', col='tratamento', kind="box",  height=15)

## MACHINE LEARNING
# We are going to try to discover each signature (each row) we want discover is active_moa is TRUE or FALSE
# We area going to use LOGISTIC REGRESSION
# Logistic regression is a statistical model that in its basic form uses a logistic function to model a binary dependent variable, although many more complex extensions exist. 
#    In regression analysis, logistic regression (or logit regression) is estimating the parameters of a logistic model (a form of binary regression).


# Tool used gonna be Scikit-learn
from sklearn.linear_model import LogisticRegression
# Toll used fo training the DataFrame
from sklearn.model_selection import train_test_split

# Instanciate a model
model_rlogistic = LogisticRegression(max_iter=1000000)



# Training the model LOGISTIC REGRESSION
# x = label (signatures)

# Select 'genic expression' (g-X) and 'celule viabililty' (c-X)
x = data_merged.select_dtypes('float64') 

# y = output
y = data_merged['active_moa']

# Spliting data for training and data for testing
x_trained, x_tested, y_trained, y_tested = train_test_split(x,y, test_size = 0.3, stratify=y, random_state = 999)

# Traininig my model
model_rlogistic.fit(x_trained,y_trained)

# checking the behaviour of my model (model accurate)
model_rlogistic.score(x_tested, y_tested)

train_test_split(x,y)

# Importing a Dummy classifier as comparator base (using a simple prediction)
from sklearn.dummy import DummyClassifier

# Calculate the accuracy
from sklearn.metrics import accuracy_score

model_dummyClassifier = DummyClassifier('most_frequent')

# Training the model Dummy
# x = label (signatures)

# Select 'genic expression' (g-X) and 'celule viabililty' (c-X)
x_dummy = data_merged.select_dtypes('float64') 

# y = output
y_dummy = data_merged['active_moa']

# Spliting data for training and data for testing
x_trained_dummy, x_tested_dummy, y_trained_dummy, y_tested_dummy = train_test_split(x_dummy,y_dummy, test_size = 0.3, stratify=y, random_state = 999)

# Traininig my model
model_dummyClassifier.fit(x_trained_dummy,y_trained_dummy)

predict_dummy = model_dummyClassifier.predict(x_tested_dummy)

accuracy_score(y_tested_dummy, predict_dummy)

data_merged['active_moa'].value_counts(normalize=True)

# Training the model DECISION TREE
from sklearn.tree import DecisionTreeClassifier
# x = label (signatures)

# Select 'genic expression' (g-X) and 'celule viabililty' (c-X)
x_dTree = data_merged.select_dtypes('float64') 

# y = output
y_dTree = data_merged['active_moa']

# Spliting data for training and data for testing
x_trained_dTree, x_tested_dTree, y_trained_dTree, y_tested_dTree = train_test_split(x_dTree,y_dTree, test_size = 0.3, stratify=y, random_state = 999)

# Traininig my model
model_dTree = DecisionTreeClassifier(max_depth=3)
model_dTree.fit(x_trained_dTree,y_trained_dTree)

model_dTree.score(x_tested_dTree, y_tested_dTree)

# ploting a decision tree
from sklearn import tree
fig, ax = plt.subplots(figsize=(15,10), facecolor='k')
tree.plot_tree(model_dTree, ax = ax , fontsize = 10, rounded=True, filled=True, feature_names=x_trained_dTree.columns, class_names=['Não Ativado', 'Ativado'])
plt.show()

# Training the model DECISION TREE
from sklearn.tree import DecisionTreeClassifier
# x = label (signatures)

# Select 'genic expression' (g-X) and 'celule viabililty' (c-X)
x_dTree2 = data_merged.select_dtypes('float64') 

# y = output
y_dTree2 = data_merged['active_moa']

# Spliting data for training and data for testing
x_trained_dTree_In_Loop, x_tested_dTree_In_Loop, y_trained_dTree_In_Loop, y_tested_dTree_In_Loop = train_test_split(x_dTree,y_dTree, test_size = 0.3, stratify=y, random_state = 999)

tested_values=[]
trained_values=[]
# Traininig my model between 3 to 30 depth
for i in range(1,30):
  model_dTree = DecisionTreeClassifier(max_depth=i)
  model_dTree.fit(x_trained_dTree_In_Loop,y_trained_dTree_In_Loop)
  tested_values.append(model_dTree.score(x_tested_dTree_In_Loop, y_tested_dTree_In_Loop))
  trained_values.append(model_dTree.score(x_trained_dTree_In_Loop, y_trained_dTree_In_Loop))

tested_values

trained_values

sns.lineplot(x=range(1,30), y=tested_values, label= 'tested_values')
sns.lineplot(x=range(1,30), y=trained_values, label= 'trained_values')

# RANDOM FOREST Model
# Build many decisions tree

from sklearn.ensemble import RandomForestClassifier
# x = label (signatures)

pd.get_dummies(data_merged, columns=['tratamento', 'dose', 'tempo'])

# Dropping unnecessary data
x_rForest = data_merged.drop(['id','n_moa', 'active_moa', 'composto'], axis=1) 

# Converting Strings to boolean values following fields
x_rForest = pd.get_dummies(x_rForest, columns=['tratamento', 'dose', 'tempo'])

# y = output
y_rForest = data_merged['active_moa']

# Spliting data for training and data for testing
x_trained_rForest,  x_tested_rForest , y_trained_rForest,  y_tested_rForest  = train_test_split(x_rForest ,y_rForest , test_size = 0.3, stratify=y, random_state = 999)

model_rForest  = RandomForestClassifier(max_depth=10)
model_rForest.fit(x_trained_rForest, y_trained_rForest) 
model_rForest.score(x_trained_rForest, y_trained_rForest)


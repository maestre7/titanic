import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

st.set_option("deprecate.showPyplotGlobalUse", False)


variables=['Pclass', 'Age', 'Sex', 'SibSp', 'Parch', 'Fare', 'CabinBool', 'Embarked_C',
'Embarked_S', 'Embarked_Q']
X = train_df[variables]
y = train_df['Survived']





#3 importar bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree

#3 Importar datos
df = pd.read_csv("Data_Set_Titanic.csv")

#3 Separar los datos y el resultado (X es mayuscula porque contiene todas las x)
X = df.drop(["Survived", "Name", "Ticket"], axis=1)
print(X.head())
y = df.Survived

#1 Crear arbol
#modelo = DecisionTreeClassifier(max_depth=6)

#1 Entrenar a la maquina
#modelo.fit(X,y)
#predicciones = modelo.predict(X)
#print(accuracy_score(y,X))

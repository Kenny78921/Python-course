
#3 importar bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree


#3 Importar datos
df = pd.read_csv("Python_Total_Titanic.csv")

#3 Separar los datos y el resultado (X es mayuscula porque contiene todas las x)
X = df.drop("Sobreviviente", axis=1)
y = df.Sobreviviente

#1 Crear arbol
modelo = DecisionTreeClassifier(max_depth=6, random_state=11)

#1 Entrenar a la maquina
modelo.fit(X,y)

pred_y = modelo.predict(X)
print("Precisión: ", accuracy_score(pred_y,y))

#2 Creamos una matriz de confusión
print(confusion_matrix(y,pred_y))
disp = ConfusionMatrixDisplay(confusion_matrix(y,pred_y, normalize="true"))
disp.plot(cmap="pink", values_format=".2f")
plt.show()

#2 Creamos el arbol de decisiones y lo graficamos
plt.figure(figsize=(12,12))
tree.plot_tree(modelo, filled=True, feature_names=X.columns, fontsize=9)
plt.show()

#2 Creamos una grafica de barras para ver la importancia de los datos
importancias = modelo.feature_importances_
columnas = X.columns
sns.barplot(x = columnas, y = importancias, color="Pink")
plt.title("Importancias de los atributos")
plt.show()
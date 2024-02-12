# -*- coding: utf-8 -*-
"""
SML: Linear Regression
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#Reading the data
df=pd.read_csv("/content/Salary_Data.csv")
df

df.columns

X=df.loc[:,['YearsExperience']]
y=df.loc[:,['Salary']]
print(y)

model=LinearRegression()

model.fit(X,y)

model.score(X,y)

#plotting the entire salary data
plt.scatter(X,y, color='red')
plt.plot(X,model.predict(X))
plt.title('Linear Regression')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

from sklearn.model_selection import train_test_split
X_train , X_test, y_train , y_test= train_test_split(X , y , test_size=0.3,random_state=0)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train),columns=X_train.columns)
X_test = pd.DataFrame(scaler.transform(X_test),columns=X_test.columns)

from sklearn.linear_model import LinearRegression
#create the model instance
model= LinearRegression()
#fitting the model on the training data
model.fit(X_train, y_train)
#model.fit(X_train, y_train.values.reshape(-1,))

model.score(X_test, y_test)

#Plotting the testing data
plt.scatter(X_test,y_test, color='red')
plt.plot(X_test,model.predict(X_test))
plt.title('Linear Regression')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

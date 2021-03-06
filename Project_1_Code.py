# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 17:17:24 2021

@author: Shreyas S
"""

#IMPORTING THE LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt




data=pd.read_csv("advertising.csv")
data.head()


#To visualise data
fig , axs =plt.subplots(1,3,sharey = True)
data.plot(kind='scatter',x='TV',y='Sales',ax=axs[0],figsize=(14,7))
data.plot(kind='scatter',x='Radio',y='Sales',ax=axs[1])
data.plot(kind='scatter',x='Newspaper',y='Sales',ax=axs[2])




#Creating x and y for linear regression
feature_cols=['TV']
X = data[feature_cols]
y = data.Sales



#Importing linear regression algorithm for simple linear regression
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)

print(lr.intercept_)
print(lr.coef_)



result = 6.9748214882298925+0.05546477*50
print(result)




#Create a dataframe with min and max valu of the table
X_new = pd.DataFrame({'TV':[data.TV.min(),data.TV.max()]})
X_new.head()


preds = lr.predict(X_new)
preds

data.plot(kind='scatter',x='TV',y='Sales')
plt.plot(X_new,preds,c='yellow',linewidth=3)

import statsmodels.formula.api as smf
lm = smf.ols(formula= 'Sales ~ TV',data=data).fit()
lm.conf_int()


#Finding the probability values
lm.pvalues


#Finding the R squared values
lm.rsquared


#Multi linear regression
feature_cols=['TV','Radio','Newspaper']
X = data[feature_cols]
y = data.Sales

lr = LinearRegression()
lr.fit(X,y)

print(lr.intercept_)
print(lr.coef_)



lm = smf.ols(formula='Sales ~ TV+Radio+Newspaper',data=data).fit()
lm.conf_int()
lm.summary()






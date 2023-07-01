#!/usr/bin/env python
# coding: utf-8

# # Question 1
Explain the difference between simple linear regression and multiple linear regression.Provide examples of each
# Answer:
Simple Linear Method is a statistical method that analyses the relationship between two 
continoius variables by fitting a linear equation to the data.
It estimates the relationship between the dependent variable (y)and the independent variable(x)by 
finding the best fit line that minimizes the sum of squared errors between the observed data points 
and predicted values.For example:lets say yoiu want to predict the persons weight (y)based on their height(x).
    You can collect data of 20 individuals and plot a scatter plot.
    You can then use simple linear regression to find the equation of the line that best fits the data.
    
# #Multiple Linear Regression::
# It is a statistical method that analyses the relationship between multiple independent variables
# (x1,x2,x3,etc)and a single dependent variable (Y).It estimates the effect of each independent variable
# on the dependent variable for controlling for the effects of other independent variables.
# 
For example,lets say you want to predict a persons salary (y)based on their education level(x1),yrs of exp(x2),
gender(x3).You can collect data on 100 individuals and can use multiple linear regression to find the equation that best 
fits the data and can be used to predict a persons salary based on their education level.,yrs of exp and gender
# In[ ]:





# # QUESTION 2:
# Discuss the assumptions of linear regression. How can you check whether these assumptions hold in
# a given dataset?

# # answer:
# The assumptions of linear regession are:
# 
Linearity: The relationbship between the dependent and the independent variable nis linear.This 
means that the relation between the dependent variable and each independent variable should
be approximately straight line.
Independence:The observations are independent of each other.This means that the value of the
    dependent variable for one observation should not be related with thedependent variable for another
    obeservation.Normality: The errors are normally distributed. This means that the distribution of the residuals should be approximately normal.

No Multicollinearity: There is no perfect multicollinearity between the independent variables. This means that the independent variables should not be highly correlated with each other.

To check whether these assumptions hold in a given dataset, various diagnostic tests can be performed. These tests include:

Residual plots: plotting the residuals against the predicted values and independent variables to detect patterns that violate the assumptions of linearity, homoscedasticity, and normality.

Normal probability plots: plotting the residuals against the expected normal distribution to check for normality.

Outlier detection: identifying and examining the influence of outliers on the regression model.
# In[ ]:





# # Q3.
# How do you interpret the slope and intercept in a linear regression model? Provide an example using
# a real-world scenario.

# # Answer:

# In a linear regression model, the slope and intercept represent the relationship between the dependent variable and independent variable(s). Specifically:
The intercept("b0")represents the predicted value of the dependent variable when all independent variables are equal to zero.It is the point where the regression line intewrsects the y axis.


The slope ("b1") represents the change in the dependent variable for each one unit increase in the independent variable.
the steepness of the regression line and reflects the strength and direction of the relationship between the dependent variable and the independent variable
# Here is an example using a real-world scenario:
# 
# Suppose we want to understand the relationship between a person's height (independent variable) and their weight (dependent variable). We collect data on 50 individuals and use a simple linear regression model to analyze the data. The regression model provides the following output:
# 
# Intercept (b0) = 50
# Slope (b1) = 2
# 
# Interpretation:
# 
# The intercept (50) represents the predicted weight of a person with a height of zero, which is not meaningful in this context. Therefore, we do not interpret the intercept in this example.
# 
# The slope (2) represents the predicted increase in weight for each one-unit increase in height. So, for every one-inch increase in height, we predict an increase of two pounds in weight. This means that the relationship between height and weight is positive and strong.

# In[ ]:





# # Question No. 4:
# Explain the concept of gradient descent. How is it used in machine learning?

# Gradient Descent is a popular optimization algorithm sed in machine learning to minimize the cost function or the objective function. The goal of gradient descent is to find the optimal values of the parameters (also called weights) that minimize the cost function and make accurate predictions on new data.
# 
# Gradient descent is used in many machine learning algorithms, such as linear regression, logistic regression, neural networks, and support vector machines. By minimizing the cost function using gradient descent, we can find the optimal values of the parameters that maximize the accuracy of the model on the training data and generalize well to new data.

# # Question No. 5:
# Describe the multiple linear regression model. How does it differ from simple linear regression?

# In a multiple linear regression model,we predict the value of dependent variables based on twpo or 
# three independent variables.It is an extension of the simple linear regresssion model,which predicts
# th3e value of the dependent var5iavble based on singlr independent variable.
# 

# The multiple linear regression model differs from the simple linear regression model in several ways.
# 
# Firstly, the multiple linear regression model involves multiple independent variables instead of just one. This means that the model can capture more complex relationships between the dependent and independent variables, allowing us to control for the effects of other variables on the dependent variable.
# Secondly, the multiple linear regression model requires more parameters to estimate (i.e., b1, b2, ..., bp), which makes the model more complex and computationally intensive.

# In[ ]:





# In[ ]:





# Question No. 6:
# Explain the concept of multicollinearity in multiple linear regression. How can you detect and address this issue?
# 
# Answer:
# Multicollinearity refers to a situation in which two or more independent variables in a multiple linear regression model are highly correlated with each other. This can cause problems in the model, such as making it difficult to interpret the coefficients of the variables and reducing the accuracy of the model's predictions.
# 
# Detecting multicollinearity can be done using several methods, such as:
# 
# Correlation matrix: A correlation matrix can be used to identify the correlation between the independent variables. If two or more variables have a high correlation coefficient (close to 1 or -1), it suggests that there may be multicollinearity in the model.
# 
# Variance Inflation Factor (VIF): The VIF is a measure of the extent to which the variance of the estimated regression coefficients is inflated due to multicollinearity. A VIF value greater than 5 or 10 suggests that there may be multicollinearity in the model.
# 
# Eigenvalues: The eigenvalues of the correlation matrix can be used to detect multicollinearity. If one or more eigenvalues are close to zero, it suggests that there may be multicollinearity in the model.
# 
# Some of the ways we can address this issue are:
# 
# Drop one or more of the highly correlated variables: One way to address multicollinearity is to drop one or more of the highly correlated variables from the model. This can help to reduce the correlation between the remaining variables and improve the accuracy of the model's predictions.
# 
# Combine the highly correlated variables: Another way to address multicollinearity is to combine the highly correlated variables into a single variable. For example, if two variables measure the same concept but in different ways, we can create a composite variable that captures both concepts.
# 
# Regularization: Regularization techniques, such as Ridge Regression and Lasso Regression, can be used to address multicollinearity by penalizing the magnitude of the regression coefficients. This can help to reduce the impact of the highly correlated variables and improve the accuracy of the model's predictions.

# In[ ]:




Question No. 7:
Describe the polynomial regression model. How is it different from linear regression?

Answer:
A polynomial regression model is a type of regression analysis that allows for non-linear relationships between the dependent variable and one or more independent variables. Unlike linear regression, which assumes a linear relationship between the dependent variable and the independent variables, polynomial regression can model more complex relationships.

The main difference between linear regression and polynomial regression is the nature of the relationship between the dependent variable and the independent variable. In linear regression, the relationship is assumed to be linear, while in polynomial regression, the relationship can be non-linear and can take on a more complex shape. Polynomial regression allows for more flexibility in modeling the relationship between the variables and can provide a better fit to the data when the relationship is non-linear.
# In[ ]:




Question No. 8:
What are the advantages and disadvantages of polynomial regression compared to linear regression? In what situations would you prefer to use polynomial regression?

Answer:
Advantages of polynomial regression:

Flexibility: Polynomial regression can model non-linear relationships between the dependent and independent variables, allowing for more flexibility in modeling complex relationships.
Higher accuracy: Polynomial regression can provide a better fit to the data when the relationship between the variables is non-linear, leading to higher accuracy of predictions compared to linear regression.
Interpretability: Polynomial regression can provide insight into the curvature of the relationship between the variables, which may be useful in certain applications.
Disadvantages of polynomial regression:

Overfitting: Higher degree polynomial functions can easily overfit the data and may not generalize well to new data, leading to poor performance on test data.
Extrapolation: Polynomial regression can be prone to errors when used for extrapolation, as the relationship between the variables may not be well-defined outside the range of the data used to train the model.
Model selection: Selecting the degree of the polynomial can be challenging, as a higher degree polynomial may lead to overfitting, while a lower degree polynomial may not capture the true relationship between the variables.
# In[ ]:





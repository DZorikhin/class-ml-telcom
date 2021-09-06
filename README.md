# Telco Customer Churn
Interactive web app could be found
[here.](https://churn-prediction-dz.herokuapp.com/)

## Context
Predict behavior to retain customers.
[Project on Kaggle.](https://www.kaggle.com/blastchar/telco-customer-churn)

## Content
Each row represents a customer, each column contains customer’s attributes described on the column Metadata.

The data set includes information about:

Customers who left within the last month – the column is called Churn
Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
Demographic info about customers – gender, age range, and if they have partners and dependents

## General Conclusions
Recall has been chosen as a target metric because there is a need to minimize the risk of skipping any positive result. In other words, we would like to prevent the situation such as model predicts that there is no churn for particular client when is fact that client had churn.

Proposed portrait of client for high churn rate: client with month-to-month contract, using fiber optic as internet service, without partner, using electronic check as payment method, recently started using company services.

The most accurate algorithm RandomForestClassifier has recall metric equal to 76%

![first](https://github.com/DZorikhin/ml-telecom/blob/master/pearson_correlation_coef.png "first")

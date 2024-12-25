# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:53:38 2024

@author: pujad
"""
import pandas as pd

# List of products
products = ['KP281','KP481','KP781']
aerofit_df = pd.read_csv("aerofit_treadmill_data.csv")

for product in products:
    # Filter product
    product_df = aerofit_df[aerofit_df['Product'] == product]
    # Contingency table over Gender and marital status
    crosstab_gender_marital_status = pd.crosstab(product_df['Gender'], product_df['MaritalStatus'],margins = True)
    print("----------------------------------------")
    print(product)
    print("----------------------------------------")
    print(crosstab_gender_marital_status)
    # Marginal Probability
    for row in crosstab_gender_marital_status.index:
        if row != 'All': # Filter Marginal Probability with 'All' as row 
            marginal_prob_row = round(crosstab_gender_marital_status.loc[row,'All']/crosstab_gender_marital_status.loc['All','All'],2)
            print(f"Marginal Probability P({row}): {marginal_prob_row}")
    for column in crosstab_gender_marital_status.columns:
        if column != 'All': # Filter Marginal Probability with 'All' as column
            marginal_prob_column = round(crosstab_gender_marital_status.loc['All',column]/crosstab_gender_marital_status.loc['All','All'],2)
            print(f"Marginal Probability P({column}): {marginal_prob_column}")
    # Conditional Probability
    for row in crosstab_gender_marital_status.index:
        for column in crosstab_gender_marital_status.columns:
            if row != 'All' and column != 'All': # Filter Conditional Probabilities with 'All' as row or column
                cond_prob_row_given_column = round(crosstab_gender_marital_status.loc[row,column] / crosstab_gender_marital_status.loc['All',column],2)
                print(f"Conditional Probability P({row} | {column}): {cond_prob_row_given_column}")
                cond_prob_column_given_row = round(crosstab_gender_marital_status.loc[row,column] / crosstab_gender_marital_status.loc[row,'All'],2)
                print(f"Conditional Probability P({column} | {row}): {cond_prob_column_given_row}")
    






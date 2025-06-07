import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder
import os

INPUT = '../data/transactions.csv'
OUTPUT = '../data/fraud_output.csv'

def detect_fraud(df):
    df['hour'] = df['time'].apply(lambda x: int(x.split(":")[0]))
    df['is_fraud'] = 0

    # Rule 1: High value
    df.loc[df['amount'] > 5000, 'is_fraud'] = 1

    # Rule 2: Odd hour transactions with high amount
    df.loc[df['hour'].isin([0,1,2,3,4]) & (df['amount'] > 3000), 'is_fraud'] = 1

    # Rule 3: Device change for same user
    df['device_change'] = df.groupby('user_id')['device_id'].transform(lambda x: x != x.shift())
    df.loc[df['device_change'] == True, 'is_fraud'] = 1

    df = df.drop(columns=['device_change'])

    return df

def apply_smote(df):
    e

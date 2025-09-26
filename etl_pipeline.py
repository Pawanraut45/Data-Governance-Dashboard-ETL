# scripts/etl_pipeline.py
import pandas as pd
import sqlite3
from sqlalchemy import create_engine


engine = create_engine('sqlite:///data/demo.db')


# load raw
df = pd.read_csv('data/sample_raw_transactions.csv', parse_dates=['created_at'])


# simple QC
qc = []
qc.append(('missing_amount', df['amount'].isna().sum()))
qc.append(('neg_amount', (df['amount'] < 0).sum()))
qc.append(('invalid_email', df['email'].str.contains('@').fillna(False).eq(False).sum()))


print('QC checks:', qc)


# basic cleaning
df_clean = df.dropna(subset=['amount'])


# flag PII exposure
df_clean['email_masked'] = df_clean['email'].str.replace(r'(^[^@]{1}).+(@.+$)', r'\1***\2', regex=True)


# write curated
df_clean.to_sql('transactions_curated', engine, if_exists='replace', index=False)
print('wrote curated data to sqlite demo.db')
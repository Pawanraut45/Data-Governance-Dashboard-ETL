# scripts/generate_sample_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


np.random.seed(42)
N = 1000
start = datetime(2024,1,1)


data = {
'tx_id': range(1, N+1),
'user_id': np.random.randint(1, 200, size=N),
'amount': np.round(np.random.exponential(50, N),2),
'currency': np.random.choice(['USD','EUR','INR'], size=N, p=[0.6,0.2,0.2]),
'created_at': [start + timedelta(minutes=int(x)) for x in np.random.randint(0, 60*24*365, N)],
'email': [f'user{u}@example.com' for u in np.random.randint(1, 500, N)],
}


# inject some bad rows
for i in range(0, 10):
data['amount'][i] = None


pd.DataFrame(data).to_csv('data/sample_raw_transactions.csv', index=False)
print('sample data written to data/sample_raw_transactions.csv')
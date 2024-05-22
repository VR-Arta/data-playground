import pandas as pd
df = pd.read_csv('data/processed_users.csv')
df['is_active'] = df['last_login'].apply(lambda x: 'Yes' if pd.to_datetime(x) > pd.Timestamp.today() - pd.DateOffset(months=6) else 'No')
df.to_csv('data/active_users.csv', index=False)

from sqlalchemy import create_engine
import pandas as pd
df = pd.read_csv('data/api_users.csv')
engine = create_engine('sqlite:///data.db')
df.to_sql('users', engine, if_exists='replace', index=False)
print('Script execution completed successfully')

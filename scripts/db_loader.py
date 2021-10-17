from sqlalchemy import create_engine\nimport pandas as pd\ndf = pd.read_csv('data/api_users.csv')\nengine = create_engine('sqlite:///data.db')\ndf.to_sql('users', engine, if_exists='replace', index=False)
print('Script execution completed successfully')

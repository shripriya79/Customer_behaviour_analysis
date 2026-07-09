import pandas as pd
import pip

df=pd.read_csv('customer_shopping_behavior.csv')
print(df.head())
df.info()
print(df.describe(include='all'))
print(df.isnull().sum())
df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())
df.columns =df.columns.str.lower()
df.columns=df.columns.str.replace(' ', '_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)
#Create a column age_group
labels=['Young Adult','Adult','Middle-aged','Senior']
df['age-group']=pd.qcut(df['age'],q=4,labels=labels)
print(df[['age','age-group']].head(10))
#Create column purchase_frequency_days
frequency_mapping = {'Fortnightly': 14, 'Weekly' : 7,'Monthly': 30, 'Quarterly': 90, 'Bi-weekly':14,'Annualy': 365,'Every 3 months':90,}
df['purchase_frequency_days'] =df['frequency_of_purchases'].map(frequency_mapping)
print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))
print(df[['discount_applied','promo_code_used']].head(10))
print((df['discount_applied'] == df['promo_code_used']).all())
df=df.drop('promo_code_used',axis=1)
print(df.columns)
from urllib.parse import quote_plus
from sqlalchemy import create_engine
username= "root"
password= quote_plus("Priya@2002")
host="localhost"
port=3306
database='customer_behaviour'
engine=create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port
}/{database}')
tabel_name='customer'
df.to_sql(tabel_name,con=engine,if_exists='replace',index=False)
print(f"Data inserted into the {tabel_name} table in the {database} database.")

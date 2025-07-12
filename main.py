import pandas as pd
import sqlalchemy as db
import makeurl

#convert excel to csv
df = pd.read_excel(r"C:\Users\ASUS\Downloads\FSI-2023-DOWNLOAD.xlsx")
print(df.head())

#convert excel to sql
engine = db.create_engine(makeurl.url_object)

excel_sql=df.to_sql("excel_sql_2",con=engine)

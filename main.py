import pandas as pd
import sqlalchemy as db
import cred

#convert excel to csv
df = pd.read_excel(r"C:\Users\ASUS\Downloads\FSI-2023-DOWNLOAD.xlsx")
print(df.head())




#excel_csv=df.to("excel_csv_geany")
#excel_sql=df.to_sql("excel_sql")

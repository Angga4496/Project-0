import pandas as pd
import sqlalchemy as db
import sys
sys.path.append('c:\\Users\\ASUS\\OneDrive\\Documents\\python project\\credentials')
import makeurl

print(makeurl.url_object)
print("path")
print(sys.path)

#convert excel to dataframe
df = pd.read_excel(r"C:\Users\ASUS\Downloads\FSI-2023-DOWNLOAD.xlsx")

##convert excel to csv
excel_csv = df.to_csv("excel_csv")

##convert excel to sql
engine = db.create_engine(makeurl.url_object)
excel_sql=df.to_sql("excel_sql_ultimate",con=engine)


'''' in this code I will demonstrate
 how to select data from database by sqlalchemy
 after (clean , analyze,aggregate,..) it using sql server
 to visualize it using plotly express in python.
 
note: I didn't use real database connection
   string for security reasons, so don't think
 that I didn't mean that when you read the code
and see things like I didn't wrote real username 
 and password in the connection string.
 '''

import plotly.express as px
from sqlalchemy import create_engine 
import pandas as pd


engine = create_engine("mssql+pyodbc://@localhost/MyDatabase"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes")

query = query = """
SELECT [month],
       SUM(sales) AS total_sales
FROM sales_table
WHERE [date] >= '2026-01-01' AND [date] < '2027-01-01'
GROUP BY [month]
ORDER BY [month] ASC;
"""


df = pd.read_sql(query, engine)

# let's say I have a dataframe called df for sales
# and I want to visualize sales over months in one year
#  using plotly express
bar = px.bar(df,x='month',y='total_sales',
             title='Sales over months in one year'
            ,labels={'month':'Month','total_sales':'Total Sales'})
bar.write_html('sales_over_months.html')

# Sales Over Months

A small data project that pulls monthly sales from a **SQL Server** database, aggregates them with SQL, and visualizes the result as an interactive bar chart using **Plotly Express**.

## What it does

1. Connects to SQL Server using **SQLAlchemy** (`pyodbc` driver, Windows trusted connection).
2. Runs a SQL query that sums sales per month for a given year.
3. Loads the result into a **pandas** DataFrame.
4. Builds an interactive bar chart with **Plotly Express**.
5. Exports the chart as a standalone HTML file (`sales_over_months.html`).

## Tech stack

- Python 3.10+
- SQL Server
- SQLAlchemy
- pyodbc
- pandas
- Plotly

## Expected table structure

The query expects a table named `sales_table` with these columns:

| Column  | Type      | Description            |
|---------|-----------|------------------------|
| `date`  | date      | Date of the sale       |
| `month` | int/text  | Month of the sale      |
| `sales` | numeric   | Sales amount           |

## Setup

1. Install the dependencies:

   ```bash
   pip install pandas plotly sqlalchemy pyodbc
   ```

2. Install **ODBC Driver 17 for SQL Server** from Microsoft.

3. Edit the connection string in `sales_over_months.py` to match your server and database:

   ```python
   engine = create_engine(
       "mssql+pyodbc://@localhost/MyDatabase"
       "?driver=ODBC+Driver+17+for+SQL+Server"
       "&trusted_connection=yes"
   )
   ```

   > The example uses Windows authentication, so no username or password is stored in the code. If you need credentials, keep them in environment variables and never commit them to the repository.

## Usage

```bash
python sales_over_months.py
```

The script saves the interactive chart as `sales_over_months.html`. Open it in any browser.

## Example query

```sql
SELECT [month],
       SUM(sales) AS total_sales
FROM sales_table
WHERE [date] >= '2026-01-01' AND [date] < '2027-01-01'
GROUP BY [month]
ORDER BY [month] ASC;
```

## Possible improvements

- Compare sales across several years.
- Add a moving average line.
- Turn the chart into an interactive dashboard (Dash or Streamlit).

## Author

**Abdullah Abbas** — [GitHub](https://github.com/Abdullah1805)

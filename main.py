# STEP 1A
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")




# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""SELECT employeeNumber, lastName FROM employees""", conn)
#print(df_first_five.head())

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees""", conn)
#print(df_five_reverse.head())

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""SELECT lastName, employeeNumber ID FROM employees""", conn)
#print(df_alias.head())

# STEP 5
# Replace None with your code
df_executive = pd.read_sql(
  """
  SELECT firstName, lastName, jobTitle,
  CASE
      WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing' 
      THEN 'Executive' 
      ELSE 'Not exexutive'
  END AS role
  FROM employees""", conn)
#print(df_executive)


# STEP 6
# Replace None with your code
df_name_length = pd.read_sql(
    """
    SELECT LENGTH(lastName) AS name_length
    FROM employees;
    """, conn)
#print(df_name_length)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees;
    """, conn)
#print(df_short_title.head())

# STEP 8
# Replace None with your code
df_total_amount = pd.read_sql(
    """
    SELECT CAST(SUM(ROUND(priceEach * quantityOrdered, 0)) AS INTEGER) AS total_amount
    FROM orderdetails;
    """, conn)
sum_total_price = df_total_amount['total_amount']
#print(sum_total_price)

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql(
    """
    SELECT 
        orderDate,
        strftime('%d', orderDate) AS day,
        strftime('%m', orderDate) AS month,
        strftime('%Y', orderDate) AS year
    FROM orders;
    """, conn)
print(df_day_month_year.head())
conn.close()
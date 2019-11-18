# Import helper module
import sqlite3 as sql3

"""
Part 2 - The Northwind Database

Part 3 - Sailing the Northwind Seas
"""

# Create connection to `northwind.sqlite3` database
conn = sql3.connect("northwind_small.sqlite3")
curs = conn.cursor()


# What are the ten most expensive items (per unit price) in the database?
most_expensive_items_query = """SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""
print('What are the ten most expensive items (per unit price) in the database?')
most_expensive = curs.execute(most_expensive_items_query).fetchall()
print(most_expensive)
print('-'*50)


# What is the average age of an employee at the time of their hiring?
print('What is the average age of an employee at the time of their hiring?')
avg_age_employee_at_hiring_query = """SELECT ROUND(AVG(HireDate-BirthDate), 2) as `Average Age of Employee at Hire` 
                                      FROM Employee;"""
avg_age = curs.execute(avg_age_employee_at_hiring_query).fetchall()
print(avg_age)
print('-'*50)


print('Part 3 - Sailing the Northwind Seas')
print('-'*50)

# What are the ten most expensive items (per unit price) in the database and their suppliers?
print('What are the ten most expensive items (per unit price) in the database and their suppliers?')
most_expensive_items_supplier_query = """SELECT ProductName, UnitPrice, CompanyName
FROM Product
JOIN Supplier 
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;"""
item_supp = curs.execute(most_expensive_items_supplier_query).fetchall()
print(item_supp)
print('-'*50)


    
# What is the largest category (by number of unique products in it)?
print('What is the largest category (by number of unique products in it)?')
largest_category_query = """SELECT CategoryName, COUNT(DISTINCT ProductName) AS Count
FROM Category
JOIN Product 
ON Category.Id = Product.CategoryId
GROUP BY CategoryName
ORDER BY Count DESC
LIMIT 1;"""
large_cat = curs.execute(largest_category_query).fetchall()
print(large_cat)
print('-'*50)

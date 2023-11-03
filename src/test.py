# import pyspark class Row from module sql
import matplotlib.pyplot as plt
from IPython.display import display
from pyspark.sql import *
from pyspark.sql.functions import explode, countDistinct

# Create a SparkSession
spark = SparkSession.builder.appName("SparkSessionExample").getOrCreate()

# Create Example Data - Departments and Employees

# Create the Departments
department1 = Row(id='123456', name='Computer Science')
department2 = Row(id='789012', name='Mechanical Engineering')
department3 = Row(id='345678', name='Theater and Drama')
department4 = Row(id='901234', name='Indoor Recreation')

# Create the Employees
Employee = Row("firstName", "lastName", "email", "salary")
employee1 = Employee('michael', 'armbrust', 'no-reply@berkeley.edu', 100000)
employee2 = Employee('xiangrui', 'meng', 'no-reply@stanford.edu', 120000)
employee3 = Employee('matei', None, 'no-reply@waterloo.edu', 140000)
employee4 = Employee(None, 'wendell', 'no-reply@berkeley.edu', 160000)

# Create the DepartmentWithEmployees instances from Departments and Employees
departmentWithEmployees1 = Row(department=department1, employees=[employee1, employee2])
departmentWithEmployees2 = Row(department=department2, employees=[employee3, employee4])
departmentWithEmployees3 = Row(department=department3, employees=[employee1, employee4])
departmentWithEmployees4 = Row(department=department4, employees=[employee2, employee3])

print(department1)
print(employee2)
print(departmentWithEmployees1.employees[0].email)

# Create DataFrame from list of rows

departmentsWithEmployeesSeq1 = [departmentWithEmployees1, departmentWithEmployees2]
df1 = spark.createDataFrame(departmentsWithEmployeesSeq1)

display(df1)

# Create a second DataFrame from a list of rows

departmentsWithEmployeesSeq2 = [departmentWithEmployees3, departmentWithEmployees4]
df2 = spark.createDataFrame(departmentsWithEmployeesSeq2)

display(df2)

# Union of 2 DataFrames

unionDF = df1.unionAll(df2)
display(unionDF)

# Write the unioned DataFrame to a Parquet file

# Remove the file if it exists
# works only on databricks dbutils.fs.rm("/tmp/databricks-df-example.parquet", True)
unionDF.write.parquet("/tmp/databricks-df-example.parquet", "overwrite")

# Read a DataFrame from the Parquet file

parquetDF = spark.read.parquet("/tmp/databricks-df-example.parquet")
display(parquetDF)

# Explode the employees column

df = parquetDF.select(explode("employees").alias("e"))
explodeDF = df.selectExpr("e.firstName", "e.lastName", "e.email", "e.salary")

display(explodeDF)

# Use filter() to return only the rows that match the given predicate

filterDF = explodeDF.filter(explodeDF.firstName == "xiangrui").sort(explodeDF.lastName)
display(filterDF)

# More filters

from pyspark.sql.functions import col, asc

# Use `|` instead of `or`
filterDF = explodeDF.filter((col("firstName") == "xiangrui") | (col("firstName") == "michael")).sort(asc("lastName"))
display(filterDF)

# Use where()-clause to filter

whereDF = explodeDF.where((col("firstName") == "xiangrui") | (col("firstName") == "michael")).sort(asc("lastName"))
display(whereDF)

# Retrieve only rows with missing firstName or lastName

filterNonNullDF = explodeDF.filter(col("firstName").isNull() | col("lastName").isNull()).sort("email")
display(filterNonNullDF)

# Replace null values with -- using DataFrame Na functions
nonNullDF = explodeDF.fillna("--")
display(nonNullDF)

# Example aggregations using agg() and countDistinct()

countDistinctDF = explodeDF.select("firstName", "lastName") \
    .groupBy("firstName", "lastName") \
    .agg(countDistinct("firstName"))

display(countDistinctDF)

# Compare the DataFrame and SQL Query Physical Plans (Hint: They should be the same.)

countDistinctDF.explain()

# Now check this result
# register the DataFrame as a temp table so that we can query it using SQL
explodeDF.createOrReplaceTempView("databricks_df_example")

# Perform the same query as the DataFrame above and return ``explain``
countDistinctDF_sql = spark.sql("SELECT firstName, lastName, count(distinct firstName) as distinct_first_names FROM databricks_df_example GROUP BY firstName, lastName")

countDistinctDF_sql.explain()

# Sum up all salaries
salarySumDF = explodeDF.agg({"salary" : "sum"})
display(salarySumDF)

# Show type
type(explodeDF.salary)

# Print the summary statistics for the salaries.

explodeDF.describe("salary").show()

# Make some nice plots using Pandas and Matplotlib

plt.clf()
pdDF = nonNullDF.toPandas()
pdDF.plot(x='firstName', y='salary', kind='bar', rot=45)
display()

# Introduction to Databases in Python

# Engines and connection strings...
# Import create_engine
from sqlalchemy import create_engine, MetaData, Table, select

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')

# # Print table names
# print(engine.table_names())

# Autoloading Tables from a database...

metadata = MetaData()

# use table object to read tables from engine
census = Table('census', metadata, autoload=True, autoload_with=engine)

# print details of table using repr() function
print(repr(census))

# Viewing Table details...

# Print the column names
print(census.columns.keys())

# Print full metadata of census
print(repr(metadata.tables['census']))

# Selecting data from a Table: raw SQL...

# Create a connection on engine
connection = engine.connect()

# Build select statement for census table: stmt
stmt = 'SELECT * FROM census'

# Execute the statement and fetch the results: results
results = connection.execute(stmt).fetchall()

# Selecting data from a Table with SQLAlchemy...

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL string
print(stmt)

# Execute the statement on connection and fetch 10 records: result
results = connection.execute(stmt).fetchmany(size=10)

# Print results
print(results)

# Handling a ResultSet...

# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by accessing it by its index
print(first_row[0])

# Print the 'state' column of the first row by using its name
print(first_row.state)



import networkx as nx
import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/Admin/Documents/Projects/Kairos/main/data/GTFS.db')

df = pd.read_sql_query('SELECT * FROM gtfs_stops', conn)

print(df.head)
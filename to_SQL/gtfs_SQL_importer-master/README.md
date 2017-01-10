Digite dentro da pasta to_SQL/src no terminal

cat gtfs_tables.sqlite  <(python import_gtfs_to_sql.py /Users/Admin/Documents/Projects/Kairos/data/sptrans  nocopy) | sqlite3 /Users/Admin/Documents/Projects/Kairos/data/GTFS.db
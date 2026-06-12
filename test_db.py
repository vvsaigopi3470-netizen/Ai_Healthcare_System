# test_db.py

import MySQLdb

conn = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="vvsg@1612",
    db="healthcare_db"
)

print("Database Connected")
import json
import psycopg2
import csv

conn = psycopg2.connect(database="cse412", user = "gatlinfarrington", password = "pass123", host = "127.0.0.1", port = "5432")

print("Opened Database")
cursor = conn.cursor()

conn.close()

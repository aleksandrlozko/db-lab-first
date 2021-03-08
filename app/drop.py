import psycopg2
from app.config import config

conn = psycopg2.connect(**config)
cur = conn.cursor()
cur.execute("DROP TABLE table_result")
cur.execute("DROP TABLE table_result")
cur.close()
conn.commit()
conn.close()
import time
import psycopg2
from app.select import select_table
from app.create import create_table
from app.populate import populate_table
from app.config import config

conn = None
retries = 30

while retries:
    try:
        conn = psycopg2.connect(**config)
        break
    except Exception as err:
        print(err)
        retries -= 1
        print('Повторная попытка -', retries)
        time.sleep(1)

try:
    create_table(conn)
    populate_table(conn)
    select_table(conn)
except Exception as err:
    print(err)
finally:
    if conn is not None:
        conn.close()
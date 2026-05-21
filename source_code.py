import os
import time
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME', 'postgres')
PING_INTERVAL = int(os.getenv('PING_INTERVAL_MINUTES', '5')) * 60
LOG_FILE = os.getenv('LOG_FILE_PATH')


def log(msg):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    full_msg = f"{timestamp} - {msg}"
    
    # Print to screen
    print(full_msg)
    
    # Save to file if specified
    if LOG_FILE:
        with open(LOG_FILE, 'a') as f:
            f.write(full_msg + '\n')

log("Pinger Started")

while True:
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        log("SUCCESS - Connected to database")
        conn.close()
    except Exception as e:
        log(f"ERROR - {e}")
    
    time.sleep(PING_INTERVAL)
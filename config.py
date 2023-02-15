import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
admin_id = int(os.getenv('ADMIN_ID'))
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
host = "localhost"

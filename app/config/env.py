import os
from dotenv import load_dotenv

# load .env file
load_dotenv()
# db informations
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_connection_string = f"host={db_host} port={db_port} dbname={db_name} user={db_user} password={db_pass}"
import os
# third party modules
import psycopg
from fastapi import FastAPI
from dotenv import load_dotenv
# custom modules
from modules import skryfall

# load .env file
load_dotenv()
# db informations
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_connection_string = "host="+db_host+" port="+db_port+" dbname="+db_name+" user="+db_user+" password="+db_pass
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome in Mtg Collection Manager API!"}

# card routes
@app.get("/cards")
async def get_cards():
    '''get all cards from database'''
    with psycopg.connect(db_connection_string) as db:
        with db.cursor() as curr:
            curr.execute("SELECT * FROM cards")
            response = curr.fetchall()
    return response

@app.get("/cards/{id}")
async def get_cards_single(id):
    '''get single card by id'''
    with psycopg.connect(db_connection_string) as db:
        with db.cursor() as curr:
            curr.execute("SELECT * FROM cards WHERE id = %s", (id))
            response = curr.fetchall()
    return response

@app.post("/cards")
async def post_cards():
    '''add cart to database'''
    with psycopg.connect(db_connection_string) as db:
        with db.cursor() as curr:
            curr.execute("SELECT * FROM cards LIMIT 10")
            response = curr.fetchall()
    return response
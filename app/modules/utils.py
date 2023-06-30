import json
import psycopg
from modules import skryfall
from psycopg.rows import dict_row
from config import env
from datetime import datetime, timedelta

def fetch_card_info(skryfall_id: str):
    ''' fetch card info by id from db or from skryfall api '''
    # check if card is in db
    with psycopg.connect(env.db_connection_string, row_factory=dict_row) as db:
        with db.cursor() as curr:
            curr.execute("""SELECT * 
                FROM card_cache
                WHERE skryfall_id = %s""", (skryfall_id,))
            cache = curr.fetchone()  
    print("=====================================")
    print(cache)
    # if card is in db, return it
    if cache: 
        card_info = json.loads(cache["skryfall_data"])
        expire = cache["expire"]
        # check if card_cache is expired
        cache_is_expired = False
        if datetime.now() > expire:
            print("cache is expired")
            cache_is_expired = True
            with psycopg.connect(env.db_connection_string, row_factory=dict_row) as db:
                with db.cursor() as curr:
                    curr.execute("""DELETE FROM card_cache WHERE skryfall_id = %s""", (skryfall_id,))
    # esle, fetch card from skryfall api and add it to db
    if not cache or cache_is_expired:
        card_info = skryfall.fetch_card_info(skryfall_id)
        expire = datetime.now() + timedelta(days=env.card_cache_expire)
        skryfall_data =  json.dumps(card_info)
        # add card to db
        with psycopg.connect(env.db_connection_string, row_factory=dict_row) as db:
            with db.cursor() as curr:
                curr.execute("""INSERT INTO card_cache 
                (skryfall_id, skryfall_data, expire) 
                VALUES (%s,%s,%s)""", (skryfall_id, skryfall_data, expire))
    return card_info

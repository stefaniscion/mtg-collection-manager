import re
import psycopg
from fastapi import FastAPI
from modules import utils
from modules import skryfall
from config import env
from schemas.card import Card

app = FastAPI()

# home route
@app.get("/")
async def root():
    return {"message": "Welcome in Mtg Collection Manager API!"}

# cards CRUD routes
@app.get("/card")
async def read_card():
    '''get all cards from database'''
    with psycopg.connect(env.db_connection_string) as db:
        with db.cursor() as curr:
            curr.execute("""SELECT * 
                FROM card
                INNER JOIN card_info ON card_info.skryfall_oracle_id = card.skryfall_oracle_id
                """)
            cards = curr.fetchall()
    return cards
@app.get("/card/{card_id}")
async def read_card_single(card_id):
    '''get a single card by id'''
    with psycopg.connect(env.db_connection_string) as db:
        with db.cursor() as curr:
            curr.execute("""SELECT * 
                FROM card
                INNER JOIN card_info ON card_info.skryfall_oracle_id = card.skryfall_oracle_id
                WHERE id = %s""", (card_id,))
            card = curr.fetchone()
    return card
@app.post("/card")
async def create_card(card: Card):
    '''add cart to database'''
    with psycopg.connect(env.db_connection_string) as db:
        with db.cursor() as curr:
            curr.execute("SELECT * FROM card LIMIT 10")
            cards = curr.fetchall()
    return cards
@app.put("/card/{card_id}")
async def update_card(card_id: int, card: Card):
    pass
@app.delete("/card/{card_id}")
async def delete_card(card_id):
    '''get a single card by id'''
    with psycopg.connect(env.db_connection_string) as db:
        with db.cursor() as curr:
            curr.execute("DELETE FROM card WHERE id = %s", (card_id,))
# cards other routes
@app.post("/card/fromlist")
async def create_card_from_card_list(card_notation_list: list):
    '''add cart to database'''
    card_list = []
    #parse card_notation_list in card_list with regex
    for card_notaton in card_notation_list:
        card = {}
        card_notaton_pattern = r"(?P<num>\d)\s(?P<card_name>[^()\n]+[^()\n\s])(\s\((?P<set>\w+)\))?"
        re_result = re.search(card_notaton_pattern, card_notaton)
        if re_result:
            card["num"] = re_result.group("num")
            card["card_name"] = re_result.group("card_name")
            card["set"] = re_result.group("set")
            card_list.append(card)
    # get needed card info from scryfall
    for card in card_list:
        if card["set"]:
            card_info = skryfall.match_card(card["card_name"], card["set"])
        else:
            card_info = skryfall.match_card(card["card_name"])
        if card_info["object"]:
            card["set"] = card_info["set"]
            card["skryfall_oracle_id"] = card_info["oracle_id"]
            card["number"] = card_info["collector_number"]
            card["language"] = card_info["lang"]
            card["mana"] = card_info["mana_cost"]
            card["text"] = card_info["oracle_text"]
            card["type"] = card_info["type_line"]
            card["image"] = card_info["image_uris"]["large"]
            card["art"] = card_info["image_uris"]["art_crop"]
        else:
            card["error"] = 1
    # update card info in database if needed
    utils.update_card_info_in_db(card_list)
    # add cards to database
    for card in card_list:
        with psycopg.connect(env.db_connection_string) as db:
            with db.cursor() as curr:
                curr.execute("""INSERT INTO card
                ("name", "set", "number", "language", quantity, skryfall_oracle_id)
                VALUES(%s, %s, %s, %s, %s, %s);""",
                (card["card_name"], card["set"], card["number"], card["language"], card["num"], card["skryfall_oracle_id"]))
    return card_list
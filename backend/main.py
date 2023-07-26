import re
import psycopg
from psycopg.rows import dict_row
from fastapi import FastAPI
from modules import utils, skryfall
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
    with psycopg.connect(env.db_connection_string, row_factory=dict_row) as db:
        with db.cursor() as curr:
            curr.execute("""SELECT * FROM card""")
            cards = curr.fetchall()
    for card in cards:
        card_info = utils.fetch_card_info(card["skryfall_id"])
        card["card_info"] = card_info
    return cards
@app.get("/card/{card_id}")
async def read_card_single(card_id: int):
    '''get a single card by id'''
    with psycopg.connect(env.db_connection_string, row_factory=dict_row) as db:
        with db.cursor() as curr:
            curr.execute("""SELECT * 
                FROM card
                WHERE id = %s""", (card_id,))
            card = curr.fetchone()
    return card
@app.post("/card")
async def create_card(card: Card):
    '''add card to database'''
    with psycopg.connect(env.db_connection_string, row_factory=dict_row) as db:
        with db.cursor() as curr:
            curr.execute("""INSERT INTO card 
                (skryfall_id, quantity, altered, foil) 
                VALUES(%s, %s, %s, %s);""", 
                (card.skryfall_id,card.quantity, card.altered, card.foil))
@app.put("/card/{card_id}")
async def update_card(card_id: int, card: Card):
    '''update card by id'''
    with psycopg.connect(env.db_connection_string, row_factory=dict_row) as db:
        with db.cursor() as curr:
            curr.execute("""UPDATE card 
                SET skryfall_id = %s, quantity = %s, altered = %s, foil = %s
                WHERE id = %s;""", 
                (card.skryfall_id,card.quantity, card.altered, card.foil, card_id))
@app.delete("/card/{card_id}")
async def delete_card(card_id: int):
    '''delete card by id'''
    with psycopg.connect(env.db_connection_string, row_factory=dict_row) as db:
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
        card["skryfall_id"] = card_info["id"]
    for card in card_list:
        with psycopg.connect(env.db_connection_string, row_factory=dict_row) as db:
            with db.cursor() as curr:
                curr.execute("""INSERT INTO card (skryfall_id, quantity, altered, foil) 
                    VALUES(%s, %s, %s, %s);""", 
                    (card["skryfall_id"],card["num"], False, False))
    return card_list
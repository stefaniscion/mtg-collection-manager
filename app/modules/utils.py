import psycopg
from config import env

def update_card_info_in_db(card_list: list):
    ''' add card info to database if needed '''
    for card in card_list:
        # check if card info already in database
        with psycopg.connect(env.db_connection_string) as db:
            with db.cursor() as curr:
                curr.execute("""SELECT *
                FROM card_info
                WHERE skryfall_oracle_id = %s""",
                (card["skryfall_oracle_id"],))
                card_info = curr.fetchone()
        # if cards info not in database, add it
        if not card_info:   
            with psycopg.connect(env.db_connection_string) as db:
                with db.cursor() as curr:
                    curr.execute("""INSERT INTO card_info
                    (name, mana_cost, text, type, skryfall_oracle_id, image, art)
                    VALUES(%s, %s, %s, %s, %s, %s, %s);""",
                    (card["card_name"], card["mana"], card["text"], card["type"], card["skryfall_oracle_id"], card["image"], card["art"]))
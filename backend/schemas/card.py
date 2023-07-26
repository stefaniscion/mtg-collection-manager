from pydantic import BaseModel

class Card(BaseModel):
    skryfall_id: str
    altered: bool = False
    foil: bool = False
    quantity: int = 1
    # card_info: dict = None
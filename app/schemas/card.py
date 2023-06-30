from pydantic import BaseModel

class Card(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image: str
    category: str
    quantity: int
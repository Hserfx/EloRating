from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from elo import update_scores

class Player(BaseModel):
    userId: str
    eloPoints: int
    place: int


app = FastAPI()

@app.post('/update_elo/')
def update_elo(players: List[Player]):
    response = update_scores(players)
    return response
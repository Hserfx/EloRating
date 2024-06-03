from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn
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

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80)
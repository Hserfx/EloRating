from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
import uvicorn
import os
from elo import update_scores

class Player(BaseModel):
    userId: str
    eloPoints: int
    eloGains: str = Field(default='0')
    place: int



app = FastAPI()


@app.post('/update_elo')
def update_elo(players: List[Player]):
    response = update_scores(players)
    return response



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")
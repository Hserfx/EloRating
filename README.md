
# EloRating API

This repository provides a simple API for calculating Elo ratings, commonly used to rank players in competitive games. The Elo rating system adjusts player ratings based on match outcomes, widely used in chess and other ranking-based games.

## Formula
The Elo rating is updated using the following formula:
```
Rn = R + K(O - P)
```
Where:
- `Rn` is the new rating
- `R` is the current rating
- `O` is the outcome (1 for win, 0 for loss)
- `P` is the expected probability of winning
- `K` is a constant that controls the adjustment's sensitivity

## Features
- **RESTful API**: Built using FastAPI for easy interaction.
- **K-factor Configuration**: Allows customization of the K-factor, which can be tuned to adjust how ratings change.
  
## Requirements
- `fastapi==0.111.0`
- `pydantic==2.7.2`
- `fastapi-cli==0.0.4`
- `uvicorn==0.27.0`

## Setup and Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/Hserfx/EloRating.git
   cd EloRating
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the API using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

4. You can access the API documentation and test the endpoints at `http://127.0.0.1:8000/docs` after starting the server.

## API Endpoints

- **`POST /calculate`**: Calculate a new Elo rating based on the current rating, opponent's rating, and match outcome.

## Example Usage

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/calculate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "current_rating": 1500,
  "opponent_rating": 1600,
  "outcome": 1
}'
```

## License
This project is licensed under the MIT License.

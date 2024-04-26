from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

TREFLE_API_KEY = "qli6VbX_vG6cfyVLp0O0MQjeqYNw-MrH-zgL173G4nw"  # Replace with your Trefle API key
TREFLE_API_URL = "https://trefle.io/api/v1/plants/search"

@app.get("/search/{query}")
async def search_plants(query: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{TREFLE_API_URL}?token={TREFLE_API_KEY}&q={query}"
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from Trefle API")






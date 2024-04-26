from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

TREFLE_API_KEY = "YOUR API KEY"  # Replace with your Trefle API key
TREFLE_API_URL = "https://trefle.io/api/v1/plants/search"

@app.get("/search/{query}")
async def search_plants(query: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{TREFLE_API_URL}?token={TREFLE_API_KEY}&q={query}"
        )
        if response.status_code == 200:
            plants = response.json().get("data", [])
            filtered_plants = []
            for plant in plants:
                filtered_plant = {
                    "scientific_name": plant.get("scientific_name", ""),
                    "description": plant.get("family_common_name", "")
                }
                filtered_plants.append(filtered_plant)
            return filtered_plants
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from Trefle API")






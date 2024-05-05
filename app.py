from typing import Optional
from fastapi import FastAPI
from spider_songs import search
from fetch_lyrics import fetch_lyrics
from urllib.parse import unquote
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/search/{query}")
def song_search(query: str):
    """
    Endpoint to search for songs
    """
    result = search(query)
    return result

@app.get("/lyrics/{url}")
async def get_lyrics(song_url: Optional[str] = None):
    if song_url:
        decoded_url = unquote(song_url)  # Decode the URL if encoded
        lyrics = fetch_lyrics(decoded_url)
        return {"lyrics": lyrics}
    else:
        return {"error": "Please provide a valid song URL."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

from fastapi import FastAPI, Query
from search import search_google

app = FastAPI()

@app.get("/search")
def search(query: str = Query(..., min_length=2)):
    return search_google(query)

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from search import search_google

app = FastAPI()

# Allow CORS for all origins (for development; restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend domain like ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search(query: str = Query(..., min_length=2)):
    return search_google(query)

import json 
from fastapi import FastAPI
from fastapi.responses import FileResponse

files = "/photos"
app = FastAPI()

@app.get("/quotes/all")
def get_all_quotes():
    with open("quotes.json", "r") as f:
        quotes = json.load(f)
    return quotes

@app.get("/quote/random")
def get_random_quote():
    with open("quotes.json", "r") as f:
        quotes = json.load(f)
    import random
    return random.choice(quotes)

@app.get("/photos/cowboy")
async def get_photo():
    return FileResponse("photos/cowboy.png")

@app.get("/photos/juice")
async def get_photo():
    return FileResponse("photos/juice.png")

@app.get("/photos/pfp")
async def get_photo():
    return FileResponse("photos/pfp.png")

@app.get("/photos/undercity")
async def get_photo():
    return FileResponse("photos/undercity.png")

@app.get("/photos/zeropointfive")
async def get_photo():
    return FileResponse("photos/zeropointfive.png")
from database.database import getAllEvents, getEventsByOwner, startConnection, endConnection
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
import os


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    os.environ.get("LOCAL_IP"),
    os.environ.get("VM_IP"),
    os.environ.get("FRONTEND_IP"),
    os.environ.get("COOKIEBOT_IP"),
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/")
def hello():
    return {"message": "You have come to coddy's lair! Bow down to the master of the code!"}

@app.get("/events")
def get_events():
    mydbAndCursor = startConnection()
    result = getAllEvents(mydbAndCursor[0])
    endConnection(mydbAndCursor)
    return result


def run_api():
    uvicorn.run(app)
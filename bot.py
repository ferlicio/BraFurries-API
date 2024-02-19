from api.api_services import run_api
from database.database import *
import sys, codecs
import threading

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
chatBot = {
    "name": "Coddy",
}


startDatabase()

run_api


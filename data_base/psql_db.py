import psycopg2
from config import URI, bot

db = psycopg2.connect(URI, sslmode ="require")
cursor = db.cursor()

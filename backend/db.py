import os

from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.environ.get("MONGO_URL")

if not MONGO_URL:
    raise RuntimeError(
        "MONGO_URL is not set. Copy .env.example, fill in the connection string, "
        "and export it before starting the API:\n"
        "    export MONGO_URL='mongodb+srv://USER:PASSWORD@HOST/?retryWrites=true&w=majority'"
    )

client = AsyncIOMotorClient(MONGO_URL)
db = client.jobgenie
job_collection = db.jobs

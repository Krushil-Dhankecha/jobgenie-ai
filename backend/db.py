from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://krushildhankecha:ptDyy0ZOQnbL1n4b@job-data.gemsau8.mongodb.net/?retryWrites=true&w=majority&appName=job-dataˀ"

client = AsyncIOMotorClient(MONGO_URL)
db = client.jobgenie
job_collection = db.jobs

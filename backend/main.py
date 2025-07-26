from fastapi import FastAPI
from scraper.linkedin import fetch_linkedin_jobs
from db import job_collection
from scraper.naukri import fetch_naukri_jobs


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "JobGenie API"}

@app.get("/scrape/linkedin")
async def scrape_linkedin():
    jobs = await fetch_linkedin_jobs()
    await job_collection.insert_many(jobs)
    return {"inserted": len(jobs)}


@app.get("/scrape/naukri")
async def scrape_naukri(query: str = "python developer", location: str = "India"):
    jobs = await fetch_naukri_jobs(query=query, location=location)
    await job_collection.insert_many(jobs)
    return {"inserted": len(jobs), "source": "Naukri"}



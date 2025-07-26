from pydantic import BaseModel

class JobListing(BaseModel):
    title: str
    company: str
    location: str
    description: str | None = None
    skills: list[str] | None = []
    url: str | None = None
    source: str

from bs4 import BeautifulSoup
import httpx

async def fetch_naukri_jobs(query="python developer", location="India", page=1):
    search_query = query.replace(" ", "%20")
    url = f"https://www.naukri.com/{search_query}-jobs-{location.lower()}-{page}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for card in soup.select("article.jobTuple"):
        title = card.select_one("a.title")
        company = card.select_one("a.subTitle")
        exp = card.select_one("li.experience")
        loc = card.select_one("li.location")
        skills = [li.text for li in card.select("ul.tags li")]

        jobs.append({
            "title": title.text.strip() if title else "",
            "company": company.text.strip() if company else "",
            "experience": exp.text.strip() if exp else "",
            "location": loc.text.strip() if loc else "",
            "skills": skills,
            "source": "Naukri",
            "url": title["href"] if title and title.has_attr("href") else None
        })

    return jobs

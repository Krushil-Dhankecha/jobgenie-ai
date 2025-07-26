from bs4 import BeautifulSoup
import httpx

async def fetch_linkedin_jobs():
    url = "https://www.linkedin.com/jobs/search/?keywords=python%20developer&location=India"
    headers = {"User-Agent": "Mozilla/5.0"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

    # Fake scraping structure (real one needs Playwright)
    jobs = []
    job_cards = soup.find_all("li", class_="result-card job-result-card")
    for card in job_cards:
        title = card.find("h3").text
        company = card.find("h4").text
        location = card.find("span", class_="job-result-card__location").text
        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "source": "LinkedIn"
        })
    print(jobs)
    return [
        {
            "title": "Machine Learning Engineer",
            "company": "Google",
            "location": "Remote",
            "link": "https://www.linkedin.com/jobs/view/12345678/"
        },
        {
            "title": "AI Researcher",
            "company": "OpenAI",
            "location": "Remote",
            "link": "https://www.linkedin.com/jobs/view/87654321/"
        }
    ]

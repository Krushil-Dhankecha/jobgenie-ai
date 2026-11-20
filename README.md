# jobgenie-ai

User
 │
 ▼
[Frontend]
 - Upload resume
 - Chat interface
 │
 ▼
[Backend API - Flask/FastAPI]
 - Resume parser
 - Job scraper
 - Query LLM
 │
 ▼
[LLM + Logic]
 - LangChain/OpenAI/Ollama
 - Skill extraction & job matching
 - Suggestion & response generation
 │
 ▼
[Job Sources]
 - LinkedIn/Naukri scraping or API


## Configuration

The API reads its MongoDB connection string from the `MONGO_URL` environment
variable. There is no default and no value in the source — it fails on startup
if the variable is not set.

```bash
cp .env.example .env          # then put the real connection string in .env
export $(grep -v '^#' .env | xargs)
uvicorn main:app --reload     # from backend/
```

`.env` is gitignored. Do not commit it.

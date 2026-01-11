# Backend (FastAPI)

This is a minimal FastAPI backend skeleton for the weather app.

Setup (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Place your API keys in `.env` or configure environment variables from `.env.example`.

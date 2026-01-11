# Frontend (Static)

This is a minimal static frontend demo that calls the FastAPI backend.

To run locally (from repository root):

```powershell
# from repo root
Set-Location .\frontend
python -m http.server 5500
# open http://127.0.0.1:5500 in your browser
```

The page will POST to `http://127.0.0.1:8000/weather` — start the backend with:

```powershell
# from repo root
Set-Location .\backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

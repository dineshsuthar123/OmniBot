"""Netlify serverless function for FastAPI using Mangum."""
import sys
from pathlib import Path
from mangum import Mangum

# Add backend root so 'app' package is importable
FUNC_DIR = Path(__file__).resolve().parent
BACKEND_DIR = FUNC_DIR.parent.parent
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.main import app
handler = Mangum(app)

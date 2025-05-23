"""Catch-all Vercel API entry forwarding any /api/* path to FastAPI app."""
import sys
from pathlib import Path

FUNC_DIR = Path(__file__).resolve().parent
BACKEND_DIR = FUNC_DIR.parent
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.main import app
handler = app

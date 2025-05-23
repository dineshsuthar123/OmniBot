"""Vercel entrypoint for FastAPI under /api/index (backend repo root)."""
import sys
from pathlib import Path

# Ensure backend root is on sys.path so `import app.main` works
FUNC_DIR = Path(__file__).resolve().parent
BACKEND_DIR = FUNC_DIR.parent
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.main import app  # ASGI app
handler = app  # optional alias

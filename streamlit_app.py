# Root wrapper so Streamlit Cloud validator is happy.
# It simply imports the actual Hub app (which sets page config).
import sys
from pathlib import Path
root = Path(__file__).resolve().parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))
import apps.hub_app.app  # noqa: F401  (executes on import)

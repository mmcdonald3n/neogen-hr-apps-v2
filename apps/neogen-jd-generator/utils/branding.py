from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class Brand:
    name: str = "Neogen"
    primary: str = "#0B5B8A"
    accent: str = "#0E7C66"
    text: str = "#111111"
    muted: str = "#667085"
    light_bg: str = "#F5F7FA"
    logo_path: str = str(Path(__file__).resolve().parents[1] / "assets" / "neogen_logo.png")
BRAND = Brand()








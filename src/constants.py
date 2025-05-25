from src import ROOT_DIR

CONFIG_DIR = ROOT_DIR / "config"
TEMPLATE_DIR = ROOT_DIR / "docs/templates"
DOWNLOAD_DIR = ROOT_DIR / "docs/downloads"

SESSION_FILE = CONFIG_DIR / "session/butter_state.json"
PPTX_TEMPLATE_PATH = TEMPLATE_DIR / "spotify-wrapped-template.pptx"

PLAYWRIGHT_START_URL = "https://www.usebutter.com/"
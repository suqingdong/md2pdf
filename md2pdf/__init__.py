import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
version_info = json.load(BASE_DIR.joinpath('version.json').open())

__version__ = version_info['version']


DEFAULT_CSS = BASE_DIR / 'styles' / 'default.css'
MERMAID_CONFIG = BASE_DIR / 'styles' / 'mermaid-config.json'

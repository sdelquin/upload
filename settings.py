from pathlib import Path

from prettyconf import config

PROJECT_DIR = Path(__file__).parent


UPLOAD_BASE_FOLDER = config('UPLOAD_BASE_FOLDER', default=PROJECT_DIR / 'target', cast=Path)
ALLOWED_EXTENSIONS = config('ALLOWED_EXTENSIONS', default=[], cast=config.list)
BUCKETS = config('BUCKETS', default={}, cast=config.json)

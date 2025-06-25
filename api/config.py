from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

config = {
    "api_port": 8000,
    "projects_source_path": f"{ROOT_DIR}/data/projects",
}
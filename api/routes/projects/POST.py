from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from api.main import db

router = APIRouter()


projects = [
    {"id": 1, "name": "Project Alpha", "description": "First project"},
    {"id": 2, "name": "Project Beta", "description": "Second project"},
]


class Project(BaseModel):
    id: int
    name: str
    description: str
    creation_date: str
    model_type: str


@router.post("", response_model=List[Project])
def get_projects():
    db.projects.insert_one({"name": "Project Gamma", "description": "Third project", "creation_date": "2023-10-01", "model_type": "Type A"})
    return projects
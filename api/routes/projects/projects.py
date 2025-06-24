from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()


projects = [
    {"id": 1, "name": "Project Alpha", "description": "First project"},
    {"id": 2, "name": "Project Beta", "description": "Second project"},
]


class Project(BaseModel):
    id: int
    name: str
    description: str


@router.get("", response_model=List[Project])
def get_projects():
    return projects
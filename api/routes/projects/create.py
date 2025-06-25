from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import datetime
from api.config import config
import os

from api.db import db

router = APIRouter()


class ProjectCreateRequest(BaseModel):
    name: str
    model_type: str

@router.post("")
def create_projects(project: ProjectCreateRequest):
    
    project_dict = project.model_dump()
    
    project_dict["created_at"] = datetime.datetime.now()
    
    resp = db.projects.insert_one(project_dict)
    
    os.mkdir(config["projects_source_path"] + "/" + str(resp.inserted_id))
    os.mkdir(config["projects_source_path"] + "/" + str(resp.inserted_id) + "/raw_data")
    os.mkdir(config["projects_source_path"] + "/" + str(resp.inserted_id) + "/labeled_data")
    os.mkdir(config["projects_source_path"] + "/" + str(resp.inserted_id) + "/datasets")
    
    return {
        "success": True,
        "data": {
            "id": str(resp.inserted_id)
        }
    }
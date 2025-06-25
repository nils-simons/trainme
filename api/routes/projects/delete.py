from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from bson import ObjectId
from api.config import config
import shutil

from api.db import db

router = APIRouter()


@router.delete("")
def delete_projects(project_id: str):
    
    
    shutil.rmtree(config["projects_source_path"] + "/" + str(project_id))
    
    
    db.projects.delete_one({"_id": ObjectId(project_id)})
    return {
        "success": True    
    }
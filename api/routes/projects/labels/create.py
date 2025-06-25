from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import datetime
from bson import ObjectId

from api.db import db

router = APIRouter()


class LabelCreateRequest(BaseModel):
    name: str
    color: str

@router.post("")
def create_label(project_id: str, label: LabelCreateRequest):
    
    project_id = ObjectId(project_id)
    
    label_dict = label.model_dump()
    
    count = db["labels"].count_documents({"project_id": project_id})
    class_id = 0
    if count > 0:
        latest_labels = db["labels"].find({"project_id": project_id}).sort("created_at", -1).limit(1)
        class_id = latest_labels[0]["class_id"] + 1
    
    label_dict["created_at"] = datetime.datetime.now()
    label_dict["project_id"] = project_id
    label_dict["class_id"] = class_id
    
    result = db["labels"].insert_one(label_dict)
    
    return {
        "success": True,
        "data": {
            "id": str(result.inserted_id)
        }
    }
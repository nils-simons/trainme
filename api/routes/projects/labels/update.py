from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import datetime
from bson import ObjectId

from api.db import db

router = APIRouter()


class LabelCreateRequest(BaseModel):
    name: str
    color: str
    class_id: int

@router.post("")
def update_label(project_id: str, label_id: str, label: LabelCreateRequest):
    
    project_id = ObjectId(project_id)
    
    label_dict = label.model_dump()

    count = db["labels"].count_documents({"project_id": project_id, "class_id": label_dict["class_id"]})
    
    if count > 0:
        return {
            "success": False,
            "error": "Class ID already exists for this project."
        }
    
    label_dict["updated_at"] = datetime.datetime.now()
    
    db["labels"].update_one(
        {"_id": ObjectId(label_id)},
        {"$set": label_dict}
    )
    
    return {
        "success": True
    }
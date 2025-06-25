from api.config import config

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from api.routes.projects import create as create_project
from api.routes.projects import delete as delete_project
from api.routes.projects.labels import create as create_label
from api.routes.projects.labels import update as update_label


app = FastAPI()

app.include_router(create_project.router, prefix="/api/projects", tags=["Projects"])
app.include_router(delete_project.router, prefix="/api/projects/{project_id}", tags=["Projects"])
app.include_router(create_label.router, prefix="/api/projects/{project_id}/labels", tags=["Labels"])
app.include_router(update_label.router, prefix="/api/projects/{project_id}/labels/{label_id}", tags=["Labels"])

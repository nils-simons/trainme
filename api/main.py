from pymongo import MongoClient
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from api.routes.projects import projects



client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["trainme"]


app = FastAPI()

app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])

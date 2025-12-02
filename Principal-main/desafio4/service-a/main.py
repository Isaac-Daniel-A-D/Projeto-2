from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI(title="Corporate Employee API")

class Employee(BaseModel):
    id: int
    name: str
    role: str
    department: str

@app.get("/employees", response_model=List[Employee])
def get_employees():
    return [
        {"id": 101, "name": "Carlos Silva", "role": "Software Engineer", "department": "IT"},
        {"id": 102, "name": "Ana Souza", "role": "Product Owner", "department": "Product"},
        {"id": 103, "name": "Roberto Diaz", "role": "UX Designer", "department": "Design"}
    ]
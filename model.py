from pydantic import BaseModel
from bson import ObjectId
from typing import Optional


class Student(BaseModel):
    name: str
    year_of_birth: int
    gender: str
    university: str
    email: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Jasmine Nguyen",
                "year_of_birth": "2000",
                "gender": "Female",
                "university": "ITMO University",
                "email": "jasmine150720@gmail.com",
            }
        }


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "year_of_birth": student["year_of_birth"],
        "gender": student["gender"],
        "university": student["university"],
        "email": student["email"],
    }


class UpdateStudent(BaseModel):
    name: Optional[str]
    year_of_birth: Optional[int]
    gender: Optional[str]
    university: Optional[str]
    email: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Jasmine Nguyen",
                "year_of_birth": "2000",
                "gender": "Female",
                "university": "ITMO University",
                "email": "jasmine150720@gmail.com",
            }
        }
        

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

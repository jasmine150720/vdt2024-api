import motor.motor_asyncio
import os
from model import Student, student_helper
import pydantic
from bson import ObjectId
from typing import List, Union, Optional, Dict, Any

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str


mongoHost = os.getenv("MONGODB_HOST", "localhost")
url = f"mongodb://{mongoHost}:27017/vdt2024"
client = motor.motor_asyncio.AsyncIOMotorClient(url)

database = client.VDT
collection = database.student

async def fetch_all_students() -> List[Dict[str, Any]]:
    students = []
    try:
        async for student in collection.find():
            students.append(student_helper(student))
    except Exception as e:
        print(f"Error fetching all students: {e}")
    return students

async def fetch_one_student(id: str) -> Optional[Dict[str, Any]]:
    try:
        student = await collection.find_one({"_id": ObjectId(id)})
        if student:
            return student_helper(student)
    except Exception as e:
        print(f"Error fetching student with id {id}: {e}")
    return None

async def create_student(data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    try:
        student = await collection.insert_one(data)
        new_student = await collection.find_one({"_id": student.inserted_id})
        return student_helper(new_student)
    except Exception as e:
        print(f"Error creating student: {e}")
    return None

async def update_student(id: str, data: Dict[str, Any]) -> bool:
    if not data:
        return False
    try:
        student = await collection.find_one({"_id": ObjectId(id)})
        if student:
            updated_student = await collection.update_one(
                {"_id": ObjectId(id)}, {"$set": data}
            )
            return updated_student.modified_count > 0
    except Exception as e:
        print(f"Error updating student with id {id}: {e}")
    return False

async def remove_student(id: str) -> bool:
    try:
        student = await collection.find_one({"_id": ObjectId(id)})
        if student:
            await collection.delete_one({"_id": ObjectId(id)})
            return True
    except Exception as e:
        print(f"Error removing student with id {id}: {e}")
    return False

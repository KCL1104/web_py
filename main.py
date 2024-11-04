from fastapi import FastAPI, HTTPException
from config.database import user_collection
from models import User
from crud.user_crud import (
    retrieve_users,
    add_user,
    retrieve_user,
    update_user,
    delete_user,
)

app = FastAPI()

@app.get("/users", response_description="List all users")
async def get_users():
    users = await retrieve_users()
    return users

@app.post("/users", response_description="Add a new user")
async def create_user(user: User):
    new_user = await add_user(dict(user))
    return new_user

@app.get("/users/{id}", response_description="Get a single user by ID")
async def get_user(id: str):
    user = await retrieve_user(id)
    if user:
        return user
    raise HTTPException(status_code=404, detail=f"User {id} not found")

@app.put("/users/{id}", response_description="Update a user")
async def update_user_data(id: str, user: User):
    updated = await update_user(id, dict(user))
    if updated:
        return f"User {id} updated successfully"
    raise HTTPException(status_code=404, detail=f"User {id} not found")

@app.delete("/users/{id}", response_description="Delete a user")
async def delete_user_data(id: str):
    deleted = await delete_user(id)
    if deleted:
        return f"User {id} deleted successfully"
    raise HTTPException(status_code=404, detail=f"User {id} not found")

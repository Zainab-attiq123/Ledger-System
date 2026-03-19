from fastapi import HTTPException

fake_user = {"username": "admin", "password": "1234"}

def login(username: str, password: str):
    if username != fake_user["username"] or password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}
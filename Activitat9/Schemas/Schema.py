from pydantic import BaseModel

class User(BaseModel): 
    user_id:  int = None
    user_name: str
    user_surname: str
    user_age: int
    user_email: str

def user_schema(user) -> dict:
    return{
        "user_id": user[0],
        "user_name": user[1],
        "user_surname": user[2],
        "user_age": user[3],
        "user_email": user[4]
    }

def users_schema(users) -> list:
    return [user_schema(user) for user in users]